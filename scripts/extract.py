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
        print('  Opening file', os.path.basename(output_filename))

    try:
        out = open(output_filename, 'w')
    except IOError as e:
        print('Output file "{}" '
              'could not be created: {}.'.format(os.path.basename(output_filename),
                                                 e))
        sys.exit(0)


    # Write to file.
    if verbosity >= 2:
        print('  Writing to file',os.path.basename(output_filename))

    try:
        out.write(doc.strip())
    except IOError as e:
        print('Could not write to file {}: {}'.format(os.path.basename(output_filename),
                                                      e))
        sys.exit(0)

    out.close()

    if verbosity >= 1:
        print('Extracted plaintext from '
              '{} into {}'.format(os.path.basename(input_filename),
                                  os.path.basename(output_filename)))


if __name__ == '__main__':

    # Add extra command line arguments for this script.
    parser = argparse.ArgumentParser(
        description='Extracts plaintext from docx files',
        parents=[uweclang.BATCH_PARSER])

    parser.add_argument('-e', '--extensions',
                        nargs='*',
                        default=['.docx'],
                        metavar='ext',
                        dest='ext',
                        help='accepted file extensions for input')

    parser.add_argument('-x', '--o-extension',
                        nargs='?',
                        default='.txt',
                        metavar='oext',
                        dest='oext',
                        help='extension for output file')

    # Parse command line arguments.
    args = parser.parse_args()


    # Set default verbosity.
    if args.verbose is None:
        args.verbose = 1


    # Comnine extra '-f' files with position file arguments.
    paths = args.file
    if args.extra_files is not None:
        paths.extend(args.extra_files)


    # Setup extension checking function
    args.ext = args.ext
    def is_valid_target(file):
        return os.path.isfile(file) and os.path.splitext(file)[1] in args.ext


    # Identify all the files to process.
    files = []
    ignored_files = []
    for path in paths:
        if os.path.isdir(path):
            # Handle a directory.
            if args.verbose >= 3:
                print('Finding files in', path)

            # The os.walk call will traverse the directory producing
            # (path, dirs, files) tuples.
            targets = []
            for x in os.walk(path):
                if not args.recursive:
                    # Prevent recursive walk. This deletes all items in the
                    # list x[1] before the next level of the hierarchy is
                    # generated.
                    del x[1][:]

                # Get all files in the directory.
                targets.append([os.path.join(x[0], l) for l in x[2]])

            # Flatten the list of lists of files.
            targets = chain.from_iterable(targets)

            for x in targets:
                if args.verbose >= 3:
                    print('  Found file', path)

                # Select list based on is_valid_target, and append to it.
                # This is a bit clever...
                (ignored_files, files)[is_valid_target(x)].append(x)

        else:
            if args.verbose >= 3:
                print('Found file', path)

            # Handle a file.
            (ignored_files, files)[is_valid_target(path)].append(path)


    # Resolve absolute paths.
    if args.verbose >= 3:
        print('Resolving absolute paths...')

    files = map(os.path.abspath, files)
    out_path = os.path.abspath(args.output)


    # Print list of ignored files.
    if args.verbose >= 1:
        for x in ignored_files:
            print("Ignore file:", x)
        print('--- Begin Processing ---')


    # Process the files.
    if args.batch_mode == 'none':
        # Process each file seperately.
        for filename in files:
            name_part = os.path.splitext(os.path.basename(filename))[0]
            extract_plaintext_from_docx(filename,
                                        os.path.join(out_path,
                                                     name_part + args.oext),
                                        verbosity=args.verbose)
    else:
        # Process files in batch mode.
        uweclang.batch_process(extract_plaintext_from_docx,
                               in_files=batch_directories,
                               out_dir=out_path,
                               batch_size=args.batch_size,
                               batch_mode=args.batch_mode,
                               verbosity=args.verbose)

    if args.verbose >= 1:
        print('--- End Processing ---')
