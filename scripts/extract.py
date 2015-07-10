#! /usr/bin/env python3

import sys
import os
import argparse

import uweclang


def extract_plaintext_from_docx(input_filename, output_filename, verbosity=1):
    xml = uweclang.get_document_xml(input_filename, verbosity=verbosity)
    doc = uweclang.xml_to_plain(xml, verbosity=verbosity)


    # Open file for writing.
    if verbosity >= 2:
        print('Opening file', os.path.basename(output_filename))

    try:
        out = open(output_filename, 'w')
    except IOError as e:
        print('Output file "{}" '
              'could not be created: {}.'.format(os.path.basename(output_filename),
                                                 e))
        sys.exit(0)


    # Write to file.
    if verbosity >= 2:
        print('Writing to file',os.path.basename(output_filename))

    try:
        pass
        # out.write(doc.strip())
    except IOError as e:
        print('Could not write to file {}: {}'.format(os.path.basename(output_filename),
                                                      e))
        sys.exit(0)

    out.close()

    if verbosity >= 1:
        print('Extracted plaintext from {} to {}'.format(os.path.basename(input_filename),
                                                         os.path.basename(output_filename)))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Extracts plaintext from docx files',
        parents=[uweclang.BATCH_PARSER])


    parser.add_argument('-e', '--extensions',
                        nargs='*',
                        default='.docx',
                        metavar='ext',
                        dest='ext',
                        help='accepted file extensions for input')

    parser.add_argument('-x', '--o-extension',
                        nargs='?',
                        default='.txt',
                        metavar='oext',
                        dest='oext',
                        help='extension for output file')
    # Example args:
    # batch=10, ext='.docx', file='.', file_extra=None, output='.',
    # quiet=False, verbose=None

    args = parser.parse_args()

    # Comnine extra '-f' files with position file arguments.
    paths = list(args.file)
    if args.extra_files is not None:
        paths.extend(args.extra_files)


    # Resolve absolute paths.
    if args.verbose >= 3:
        print('Converting input paths from relative to absolute...')

    paths = map(os.path.abspath, paths)
    out_path = os.path.abspath(args.output)


    # Identify files to process.
    batch_directories = []
    single_files = []
    for path in paths:
        if os.path.isdir(path):
            print('Process directory', path)
            batch_directories.append(path)
        else:
            # Check for docx file extension:
            if os.path.splitext(path)[1] == args.ext:
                print('Process file', os.path.basename(path))
                single_files.append(path)
            else:
                print('Ignore file', path)

    # Process files:
    for filename in single_files:
        name_part = os.path.splitext(path)[0]
        extract_plaintext_from_docx(filename,
                                    os.path.join(out_path, name_part + args.oext),
                                    verbosity=args.verbose)
    # Process directories:
    if batch_directories:
        uweclang.batch_process(extract_plaintext_from_docx,
                               in_files=batch_directories,
                               out_dir=out_path,
                               batch_size=args.batch,
                               verbosity=args.verbose)
