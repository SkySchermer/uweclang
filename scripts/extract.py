#! /usr/bin/env python3

import sys
import os
import argparse
from itertools import chain

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

    if args.verbose is None:
        args.verbose = 1

    # Resolve absolute paths.
    if args.verbose >= 3:
        print('Converting input paths from relative to absolute...')

    out_path = os.path.abspath(args.output)


    def is_valid_target(file):
        return os.path.splitext(file)[1] == args.ext

    # Identify all the files to process.
    files = []
    ignored_files = []
    for path in paths:
        if os.path.isdir(path):
            # Handle a directory.

            # The os.walk call will traverse the directory. x[2] Pulls out the
            # list of files. The chain.from_iterable will flatten the list of
            # lists.
            targets = chain.from_iterable([x[2] for x in os.walk(path)])

            for x in targets:
                # Select list based on is_valid_target, and append to it.
                # This is a bit clever...
                (ignored_files, files)[is_valid_target(x)].append(x)

        else:
            # Handle a file.
            (ignored_files, files)[is_valid_target(path)].append(path)

    # Resolve absolute paths.
    files = map(os.path.abspath, files)

    # Print list of ignored files.
    if args.verbose >= 1:
        for x in ignored_files:
            print("Ignore file:", x)

    # Normal Process:
    for filename in files:
        name_part = os.path.splitext(path)[0]
        extract_plaintext_from_docx(filename,
                                    os.path.join(out_path, name_part + args.oext),
                                    verbosity=args.verbose)

    # # Batch process:
    # uweclang.batch_process(extract_plaintext_from_docx,
    #                            in_files=batch_directories,
    #                            out_dir=out_path,
    #                            batch_size=args.batch,
    #                            verbosity=args.verbose)
