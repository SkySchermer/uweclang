"""UWEC Language Tools batch tools module

    Provides functions for processing data in batches.

Module Globals:

    BATCH_PARSER: Provides a template ArgumentParser for accepting arguments
        concerning batch file processing. It provides the following setup:

        Positional Arguments:
            file: Any number of input files or directories.

        Optional Arguments:
            --file: Any number of extra input files or directories.
            --recursive: Flag to select for recursive traversal of directories.
            --output: Output directory.
            --quiet: Silence process output.
            --verbose: Select process output level.
            --batch-size: Size of batches, or number of division, depending on the batch-mode.
            --batch-mode: Select how to do batching.

"""
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

# Standard imports
import os
import errno
import argparse

from itertools import chain
from math import ceil
from pprint import pprint

# Build base for batch argument parsing.
BATCH_PARSER = argparse.ArgumentParser(add_help=False)

BATCH_PARSER.add_argument('file',
                          nargs='*',
                          default=['.'],
                          metavar='input-file',
                          help="""
    the files and directories to process. Each directory will be scanned for
    files to process.
    """)

BATCH_PARSER.add_argument('-f', '--file',
                          nargs='*',
                          default=[],
                          metavar='input-file',
                          dest='extra_files',
                          help='additional input files')

BATCH_PARSER.add_argument('-e', '--extensions',
                        nargs='*',
                        default=[''],
                        metavar='ext',
                        dest='extensions',
                        help='accepted file extensions for input')

BATCH_PARSER.add_argument('-r', '--recursive',
                          action='store_true',
                          help='search directories for input files recursively')

BATCH_PARSER.add_argument('-o', '--output-dir',
                          default='.',
                          metavar='output-dir',
                          dest='output_dir',
                          help='the output directory')

BATCH_PARSER.add_argument('-w', '--no-overwrite',
                          nargs='*',
                          metavar='ext',
                          dest='no_overwrite',
                          help="""
    existing file extensions that will prevent processing. If a file with the
    same name containing one of the given extensions exists, the process will
    skip to the next file.
    """)

_GROUP = BATCH_PARSER.add_mutually_exclusive_group()
_GROUP.add_argument('-q', '--quiet',
                    action='store_true',
                    help='silence all output')

_GROUP.add_argument('-v', '--verbose',
                    action='count',
                    help='provide detailed information')

BATCH_PARSER.add_argument('-b', '--batch-size',
                          nargs='?',
                          type=int,
                          default=10,
                          metavar='batch-size',
                          dest='batch_size',
                          help="""
    batch the output into subdirectories according to the batch-mode. The
    batch-size parameter is used together with the --batch-mode option to
    determine how many subdirectories or files per subdirectories to use.
    """)

BATCH_PARSER.add_argument('-m', '--batch-mode',
                          nargs='?',
                          choices=['none', 'count', 'divide'],
                          default='none',
                          const='count',
                          metavar='mode',
                          dest='batch_mode',
                          help="""
    sets the batch mode. By default, no batch mode is used, and all files are
    placed in the output directory. In count mode, each batch will contain at
    most the number of files specified by the --batch-size argument (default
    10). In divide mode, there will be that number of batch directories, and
    files will be divided evenly between them. If the flag is provided but no
    mode is given, count mode will be used.
    """)


# def select_files(args, file_selector=(lambda x: True)):
#     """Select files to process based upon parsed arguments from a BATCH_PARSER.

#     This function will traverse each input directory for valid files and add
#     them to a list. It will also keep track of invalid files to return for
#     reference. The behavior of this function is controlled by command line
#     arguments.

#     Arguments:
#         args (NameSpace): The parsed command line arguments to use for
#             selecting files.
#         file_selector (str -> bool): A function for determining if a file
#             should be selected or not. Defaults to accepting all files.

#     Returns:
#         (str, str): A tuple containing a list of selected filenames and a list
#             of ignored filenames.
#     """
#     # Combine extra '-f' files with position file arguments.
#     paths = args.file
#     if args.extra_files is not None:
#         paths.extend(args.extra_files)


#     # Identify all the files to process.
#     files = []
#     ignored_files = []
#     for path in paths:
#         if os.path.isdir(path):
#             # Handle a directory.
#             if args.verbose >= 3:
#                 print('Finding files in', path)

#             # The os.walk call will traverse the directory producing
#             # (path, dirs, files) tuples.
#             targets = []
#             for x in os.walk(path):
#                 if not args.recursive:
#                     # Prevent recursive walk. This deletes all items in the
#                     # list x[1] before the next level of the hierarchy is
#                     # generated.
#                     del x[1][:]

#                 # Get all files in the directory.
#                 targets.append([os.path.join(x[0], l) for l in x[2]])

#             # Flatten the list of lists of files.
#             targets = chain.from_iterable(targets)

#             for x in targets:
#                 if args.verbose >= 3:
#                     print('  Found file', path)

#                 # Select list based on file_selector, and append to it.
#                 # This is a bit clever...
#                 (ignored_files, files)[file_selector(x)].append(x)

#         else:
#             if args.verbose >= 3:
#                 print('Found file', path)

#             # Handle a file.
#             (ignored_files, files)[file_selector(path)].append(path)


#     # Resolve absolute paths.
#     if args.verbose >= 3:
#         print('Resolving absolute paths...')

#     files = map(os.path.abspath, files)

#     return (files, ignored_files)



def check_extensions(path, ext_list):
    #Check if file should be skipped.
    for ext in ext_list:
        if os.path.isfile(os.path.join(path, ext)):
            return ext
    return None

def batch_process(process, **kwargs):
                  # in_files=['.'],
                  # out_dir='.',
                  # batch_size=10,
                  # batch_mode='count',
                  # batch_dir_prefix='batch',
                  # skip_exts=None,
                  # verbosity=1):
    """Runs a process on a set of files and batches them into subdirectories.

    Arguments:
        process ((IN, OUT, Verbosity) -> str): The function to execute on each
            file.
        in_dir (Optional[str]): The input directory.
        out_dir (Optional[str]): The output directory.
        batch_size (Optional[int]): The size of each subdirectory or the number
            of subdirectories, depending on the batch_mode.
        batch_mode (Optional[str]): The batch mode. Can be one of 'count' or
            'divide'. In count mode, each batch will contain at most the number
            of files specified by the batch_size (default 10). In divide mode,
            there will be that number of batch directories, and files will be
            divided evenly between them.
        batch_dir_prefix (Optional[str]): The prefix for batch subdirectories.
        verbosity (int): The verbosity of the output.

    Returns:
        (None)
    """
    # Get values from kwargs:
    search_locations = kwargs.get('file', ['.'])
    search_locations.extend(kwargs.get('extra_files', []))
    extensions = kwargs.get('extensions', [''])
    recursive = kwargs.get('recursive', False)

    output_dir = os.path.abspath(kwargs.get('output_dir', '.'))
    no_overwrite = kwargs.get('no_overwrite', [])

    verbosity = kwargs.get('verbose', 1)
    if kwargs.get('quiet', False):
        verbosity = 0

    batch_mode = kwargs.get('batch_mode', 'none')
    batch_size = kwargs.get('batch_size', 10)

    verbosity = 3
    if verbosity >= 1:
        print('\n--- Begin Processing ---')

    # Print debug info.
    if verbosity >= 3:
        pprint(kwargs)

    print(os.path.join('abc', ''))

    if batch_mode == 'none':
        # Process each file seperately.
    #     for filename in files:
    #         name_part = os.path.splitext(os.path.basename(filename))[0]
    #         extract_plaintext_from_docx(filename,
    #                                     out_path,
    #                                     verbosity=args.verbose)
    #     return
        if verbosity >= 1:
            print('--- End Processing ---\n')

        return

    if batch_mode == 'divide':
        batch_size = ceil(len(in_files) / (batch_size))

    if verbosity >= 1:
        print('\n--- Begin Processing ---')


    # current_batch = 0
    # file_number = None
    # batch_name = None
    # batch_dir = None


    # # Process each file seperately.
    # for filename in in_files:

    #     if file_number is not None and file_number >= batch_size:
    #         current_batch += 1
    #         file_number = None

    #     if file_number is None:
    #         file_number = 0
    #         # Get details for next batch.
    #         batch_name = '{}{:03}'.format(batch_dir_prefix, current_batch)
    #         batch_dir = os.path.join(os.path.abspath(out_dir), batch_name)

    #         # Create batch directory.
    #         if verbosity >= 2:
    #             print(' -> Creating directory', batch_dir)
    #         try:
    #             os.makedirs(batch_dir)
    #         except OSError as e:
    #             if e.errno == errno.EEXIST:
    #                 pass # We don't care if directory already exists.

    #         if verbosity >= 1:
    #             print('Starting batch', current_batch)

    #     fullpath = os.path.join(batch_dir,
    #                             os.path.splitext(os.path.basename(filename))[0])
    #     f_ext = check_extensions(fullpath, skip_exts)

    #     if f_ext is None:

    #         # Process the file.
    #         process(filename,
    #                 batch_dir,
    #                 verbosity=verbosity)
    #     else:
    #         if verbosity >= 1:
    #             print('File {} already exists. Skipping process.'
    #                   ''.format(os.path.splitext(os.path.basename(path))[0]
    #                              + f_ext))

    #     file_number += 1



