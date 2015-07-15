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


def split_ext(filename):
    if not filename:
        return ''

    parts = filename.split('.')
    if parts[0] == '':
        fn = '.' + parts[1]
        exts = parts[2:]
    else:
        fn = parts[0]
        exts = parts[1:]

    exts = ['.' + x for x in exts]

    return (fn, ''.join(exts))



def get_files(search_locations, extensions, recursive=False):
    if (isinstance(search_locations, str)
        or isinstance(search_locations, unicode)):
        search_locations = [search_locations]

    search_locations = set(search_locations)

    files = [x for x in search_locations if os.path.isfile(x)]
    dirs =  [x for x in search_locations if os.path.isdir(x)]
    # Identify all the files to process.
    for item in dirs:
        print('Searching in {}'.format(item))
        if os.path.isdir(item):

            # The os.walk call will traverse the directory producing
            # (path, dirs, files) tuples.
            targets = []
            for x in os.walk(item):
                if not recursive:
                    # Prevent recursive walk. This deletes all items in the
                    # list x[1] before the next level of the hierarchy is
                    # generated.
                    del x[1][:]

                # Get all files in the directory.
                targets.append([os.path.join(x[0], l) for l in x[2]])

            # Flatten the list of lists of files.
            targets = chain.from_iterable(targets)

            for x in targets:
                if extensions is None or split_ext(x)[1] in extensions:
                    files.append(x)
        else:
            # Handle a file.
            if extensions is None or split_ext(item)[1] in extensions:
                files.append(item)

    full_files = set()
    for item in files:
        full_files.add(os.path.abspath(item))

    return ((x for x in full_files), len(full_files))


def batch_process(process, **kwargs):
                  # in_files=['.'],
                  # out_dir='.',
                  # batch_size=10,
                  # batch_mode='count',
                  # batch_dir_format='batch',
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
        batch_dir_format (Optional[str]): The format string for batch
            subdirectory names. Defaults to 'batch{:03}'
        verbosity (int): The verbosity of the output.

    Returns:
        (None)
    """
    # Get values from kwargs:
    search_locations = kwargs.get('file', ['.'])
    search_locations.extend(kwargs.get('extra_files', []))
    extensions = kwargs.get('extensions', [])
    recursive = kwargs.get('recursive', False)

    output_dir = os.path.abspath(kwargs.get('output_dir', '.'))
    no_overwrite = kwargs.get('no_overwrite', [])

    verbosity = kwargs.get('verbose', 1)
    if kwargs.get('quiet', False):
        verbosity = 0

    batch_mode = kwargs.get('batch_mode', 'none')
    batch_size = kwargs.get('batch_size', 10)
    batch_dir_format = kwargs.get('batch_dir_prefix', 'batch{:03}')

    # Get files to process
    files, file_count = get_files(search_locations,
                                  extensions,
                                  recursive)

    verbosity = 3

    # Print debug info.
    if verbosity >= 3:
        pprint(kwargs)


    # Prepare batching info
    if batch_mode == 'none':
        batch_count = 0
    elif batch_mode == 'divide':
        batch_count = batch_size
    elif batch_mode == 'count':
        batch_count = int(ceil(file_count / batch_size))

    batches = []
    for batch_num in range(0, batch_count):
        batch_name = batch_dir_format.format(batch_num)
        batch_path = os.path.join(output_dir, batch_name)
        batches.append((batch_path, batch_name))

        # Create batch directory.
        try:
            os.makedirs(batch_path)
        except OSError as e:
            if e.errno == errno.EEXIST:
                # We don't care if directory already exists.
                pass


    # Assign files to batches using (input_file, output_location)
    out = output_dir
    assigned_files = []

    for i, item in enumerate(files):
        if batch_count >= 0:
            out, short = batches[i % len(batches)]
        assigned_files.append((item, out))


    # Check for already existing outputs.
    existing = get_files(output_dir,
                         no_overwrite,
                         recursive=True)[0]

    existing = {split_ext(os.path.basename(x))[0] : x for x in existing}

    if verbosity >= 3:
        print('Process preventing extensions:',no_overwrite)

    if no_overwrite:
        if verbosity >= 1:
            print('\n--- Checking for existing files... ---')

        # Function for checking if file exists in output_dir
        def check(file_name):
            base, ext = split_ext(os.path.basename(file_name))
            over_written = existing.get(base, False)
            if over_written:
                if split_ext(os.path.basename(existing[base]))[1] in no_overwrite:
                    print('File {}{} skipped due to overwrite match:\n\t{}'
                          ''.format(base, ext, existing[base]))
                    return False
            return True

        # Filter for files that don't exist in output_dir
        assigned_files = [x for x in assigned_files if check(x[0])]


    if verbosity >= 1 and len(assigned_files) == 0:
        print('\n--- No files to process ---')
        return

    if verbosity >= 1:
        print('\n--- Begin Processing {} files ---'
              ''.format(len(assigned_files)))

    # Process each file:
    for item, out in assigned_files:
        process(item, out, verbosity=verbosity)

    if verbosity >= 1:
        print('--- End Processing ---\n')

