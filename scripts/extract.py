#! /usr/bin/env python

import sys
import os
import argparse

import uweclang


def extract_plaintext_from_docx(input_filename, output_filename, verbosity=1):
    doc = xml_to_plain(get_document_xml(input_file,
                                        verbosity=verbosity),
                       verbosity=verbosity)


    # Open file for writing.
    if verbosity >= 2:
        print('Opening file {}'.format(output_filename))

    try:
        out = open(output_file_name, 'w')
    except IOError as e:
        print('Output file "{}" '
              'could not be created: {}.'.format(output_filename, e))
        sys.exit(0)


    # Write to file.
    if verbosity >= 2:
        print('Writing to file {}'.format(output_filename))

    try:
        out.write(doc.strip())
    except IOError as e:
        print('Could not write to file: {}'.format(e))
        sys.exit(0)

    out.close()

    if verbosity >= 1:
        print('Extracted plaintext from {} to {}'.format(input_filename,
                                                         output_filename))


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

    #batch=10, ext='.docx', file='.', file_extra=None, output='.', quiet=False, verbose=None

    args = parser.parse_args()

    # Comnine extra '-f' files with position file arguments.
    paths = list(args.file)
    if args.extra_files is not None:
        paths.extend(args.extra_files)


    # Resolve absolute paths.
    if args.verbose >= 3:
        print('Converting input paths from relative to absolute...')

    paths = map(os.path.abspath, paths)


    # Process each file.
    for path in paths:
        if os.path.isdir(path):
            print('Process directory "{}"'.format(path))
        else:
            # Check for docx file extension:
            if os.path.splitext(path)[1] == '.docx':
                print('Process file "{}"'.format(path))
            else:
                print('Ignore file "{}"'.format(path))
