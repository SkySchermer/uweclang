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
            --batch: Batch-size for batch mode.
            --batch-mode: Select how to do batching.

"""

import os
import argparse
from itertools import chain


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
                          metavar='input-file',
                          dest='extra_files',
                          help='additional input files')

BATCH_PARSER.add_argument('-r', '--recursive',
                          action='store_true',
                          help='search directories for input files recursively')

BATCH_PARSER.add_argument('-o', '--output',
                          default='.',
                          metavar='output-file',
                          help='the output directory')

_GROUP = BATCH_PARSER.add_mutually_exclusive_group()
_GROUP.add_argument('-q', '--quiet',
                    action='store_true',
                    help='silence all output')

_GROUP.add_argument('-v', '--verbose',
                    action='count',
                    help='provide detailed information')

BATCH_PARSER.add_argument('-b', '--batch',
                          nargs='?',
                          type=int,
                          default=10,
                          metavar='batch-size',
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
    most the number of files specified by the --batch argument (default 10).
    In divide mode, there will be that number of batch directories, and files
    will be divided evenly between them. If the flag is provided but no mode
    is given, count mode will be used.
    """)


def _all_files(path):
    """Default file selector for select_files.

    Arguments:
        path (str): The path to a file.

    Returns:
        True
    """
    return True


def select_files(args, file_selector=_all_files):
    """Select files to process based upon parsed arguments from a BATCH_PARSER.

    This function will traverse each input directory for valid files and add
    them to a list. It will also keep track of invalid files to return for
    reference. The behavior of this function is controlled by command line
    arguments.

    Arguments:
        args (NameSpace): The parsed command line arguments to use for
            selecting files.
        file_selector (str -> bool): A function for determining if a file
            should be selected or not. Defaults to accepting all files.

    Returns:
        (str, str): A tuple containing a list of selected filenames and a list
            of ignored filenames.
    """
    # Combine extra '-f' files with position file arguments.
    paths = args.file
    if args.extra_files is not None:
        paths.extend(args.extra_files)


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

                # Select list based on file_selector, and append to it.
                # This is a bit clever...
                (ignored_files, files)[file_selector(x)].append(x)

        else:
            if args.verbose >= 3:
                print('Found file', path)

            # Handle a file.
            (ignored_files, files)[file_selector(path)].append(path)


    # Resolve absolute paths.
    if args.verbose >= 3:
        print('Resolving absolute paths...')

    files = map(os.path.abspath, files)

    return (files, ignored_files)


def batch_process(process,
                  in_files=['.'],
                  out_dir='.',
                  batch_size=10,
                  batch_mode='count',
                  batch_dir_prefix='batch',
                  verbosity=1):
    """
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
        verbosity: The verbosity of the output.
    Returns:
        None
    """
    # Process each file seperately.
    for filename in files:
        name_part = os.path.splitext(os.path.basename(filename))[0]
        extract_plaintext_from_docx(filename,
                                    os.path.join(out_path,
                                                 name_part + args.oext),
                                    verbosity=args.verbose)

