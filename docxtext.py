#! /usr/bin/env python

import sys
import os
import zipfile
import re

# Regex for identifying docx files.
docx_ext = '(.*)\.docx'


# Flags for debug printing.
debug_print = True
debug_log = True

#------------------------------------------------------------------------------

def extract_lines(docx_file):
    '''
    Extracts a list of plaintext lines from a Microsoft Word docx file.
    '''
    # This is a list of find/replace pairs for editing the docx XML data. See
    #   https://docs.python.org/2/library/re.html
    # for details.
    edits = [{'FIND': '</w:p>', 'REPLACE': '\n'},  # Preserve paragraphs.
             {'FIND': '<[^>]+>', 'REPLACE': ''},  # Remove formatting XML.
             {'FIND': '[\x7f\x80]+', 'REPLACE': ''},  # Remove non-printable characters.
             {'FIND': '\A[0-9]{7}', 'REPLACE': ''},  # Remove 7-digit number at start of file.
             {'FIND': '[“”]', 'REPLACE': '"'},  # Straighten quotes.
             {'FIND': '[‘’]', 'REPLACE': "'"},  # Straighten apostrophes/single quotes.
             {'FIND': ' +,', 'REPLACE': ","}  # Remove spaces before commas.
             ]

    with zipfile.ZipFile(docx_file) as document:
        # Open document XML from the docx (ZIP) file.
        doc = document.open('word/document.xml', "r").read().decode("utf-8")

        # Perform text substitutions on XML data:
        for edit in edits:
            doc = re.sub(edit['FIND'], edit['REPLACE'], doc)

        return doc.split('\n')


#------------------------------------------------------------------------------
inline_citation_regex = re.compile(r'\s*\((?:[\w ,.]+)\s*\d*\)')

def scrub_lines(doc_lines, log_out=sys.stdout):

    result = []
    for line in doc_lines:
        # Remove whitespace at ends of line.
        line.strip()

        # Remove numerical prefixes and alignment metadata on lines.
        if re.fullmatch('(?:center|right|left)?\d+.*', line):
            if debug_print:
                print('Removed numerical/metadata prefix:', line[:30])
            if debug_log:
                print('Removed numerical/metadata prefix:\n\t', line[:30], file=log_out)
            line = re.sub('(?:center|right|left)?\d+', '', line, count=1)

        # Remove inline citations.
        inlines = inline_citation_regex.findall(line)
        if inlines:
            for citation in inlines:
                if debug_print:
                    print('Removed inline citation: {}'.format(citation))
                if debug_log:
                    print('Removed inline citation:\n\t{}'.format(citation), file=log_out)

            line = inline_citation_regex.sub('', line)

        # Remove suspected title, citation, and date lines.
        if capitalization_density(line) > 0.06 or punctuation_density(line) > 0.05:
            if debug_print:
                print('Removed suspected Title/Citation/Date: ', line[:80])
            if debug_log:
                print('Removed suspected Title/Citation/Date:\n\t', line[:80], file=log_out)
            if re.match('writer.*memo', line, flags=re.IGNORECASE):
                result.append('<<BEGIN WRITERS MEMO>>')
            continue

        # Remove number and empty lines.
        if re.fullmatch(r'\d+|\s*', line):
            if debug_print:
                print('Removed empty line: ', line[:80])
            if debug_log:
                print('Removed empty line:\n\t', line[:80], file=log_out)

            continue

        # Print line with statistical info.
        if debug_print:
            print('Cap {:.2f}%, Punc {:.2f}%, Text: {}...'.format(capitalization_density(line)*100,
                                                                  punctuation_density(line)*100,
                                                                  line[:60]))
        if debug_log:
            print('Cap {:.2f}%, Punc {:.2f}%, Text:\n\t{}...'.format(capitalization_density(line)*100,
                                                                  punctuation_density(line)*100,
                                                                  line[:60]),
                  file=log_out)

        # Preserve what remains.
        result.append(line)

    return '\n'.join(line.strip() for line in result if line != '')

def extract_writers_memo(text):
    return text.split('<<BEGIN WRITERS MEMO>>')

#------------------------------------------------------------------------------

def punctuation_density(text):
    '''
    Returns the punctuation density of the given text.
    '''
    punctuation = r'[,.?:;\\/]'

    if len(text) == 0:
        return 0

    return len(re.findall(punctuation, text)) / len(text)

#------------------------------------------------------------------------------

def capitalization_density(text):
    '''
    Returns the wrod-starting capitalized character density of the given text.
    '''
    if len(text) == 0:
        return 0

    return len(re.findall(r'\b[A-Z]\w+', text)) / len(text)


#------------------------------------------------------------------------------

def process_files(src_dir=os.getcwd(), dest_dir=os.getcwd(), targets=[]):
    '''
    Takes a list of target docx files in src_dir and converts them to plaintext.
    Each file is scrubbed of extra data and written to a text file in dest_dir.
    '''

    processed_file_count = 0;

    # Process each file in the src_directory.
    for file_name in targets:

        # Match docx files.
        match = re.match(docx_ext, file_name)
        if match:
            src_file = src_dir + '/' + file_name
            dest_file = dest_dir + '/' + match.group(1) + '.txt'
            log_file = dest_dir + '/' + match.group(1) + '.log'
            memo_file = dest_dir + '/' + match.group(1) + '.memo.txt'
            print('Extracting {} to {}'.format(src_file, dest_file))

            # Open the dest_file, or create it.
            try:
                file_out = open(dest_file, 'w')
            except IOError as e:
                print('File "{}" could not be created: {}.'.format(dest_file, e))
                sys.exit(0)

            if debug_log:
                # Open the log_file, or create it.
                try:
                    log_out = open(log_file, 'w')
                except IOError as e:
                    print('File "{}" could not be created: {}.'.format(dest_file, e))
                    sys.exit(0)

            else:
                log_out = sys.stdout

            if debug_print:
                print('- ' * 10, file_name, '- ' * 10, )

            # Extract plain text data and write to file.
            doc = scrub_lines(extract_lines(src_file), log_out)
            doc_memo = extract_writers_memo(doc)

            try:
                file_out.write(doc_memo[0].strip())
            except IOError as e:
                print('Could not write to file: {}'.format(e))
                sys.exit(0)

            if len(doc_memo) > 1:
                # Open the log_file, or create it.
                try:
                    memo_out = open(memo_file, 'w')
                except IOError as e:
                    print('File "{}" could not be created: {}.'.format(dest_file, e))
                    sys.exit(0)

                try:
                    memo_out.write(doc_memo[1].strip())
                except IOError as e:
                    print('Could not write to file: {}'.format(e))
                    sys.exit(0)

                # Close the memo file.
                memo_out.close()

            # Close the log file, if used.
            if debug_log:
                log_out.close()

            # Close the output file.
            file_out.close()

            processed_file_count += 1;



    # Print summary.
    if processed_file_count == 0:
        print('No files processed')
    else:
        print('{}/{} files processed.'.format(processed_file_count, len(targets)))


#------------------------------------------------------------------------------

# This will only run when the script is executed as a standalone program
# (as opposed to a module import.)
if __name__ == '__main__':

    if len(sys.argv) == 2:
        # Processing a single file.
        process_files(targets=[sys.argv[1]])

    elif len(sys.argv) == 3:
        # Processing a full directory.
        process_files(src_dir=sys.argv[1],
                      dest_dir=sys.argv[2],
                      targets = os.listdir(sys.argv[1]))

    else:
        # Print usage info if not enough arguments.
        print('Usage:', sys.argv[0], 'src_directory dest_directory')
        print('Usage:', sys.argv[0], 'file')
        sys.exit(0)
