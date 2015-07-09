"""UWEC Language Tools batch tools module

    Provides functions for processing data in batches.
"""
import argparse

# Build base for batch argument parsing.
BATCH_PARSER = argparse.ArgumentParser(add_help=False)

BATCH_PARSER.add_argument('file',
                          nargs='*',
                          default='.',
                          metavar='input-file',
                          help="""
    the files and directories to process. Each directory will be scanned for
    files to process.
    """)

BATCH_PARSER.add_argument('-f', '--file',
                          nargs='*',
                          metavar='input-file',
                          dest='file_extra',
                          help='additional input files')

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
    batch the output into subdirectories of batch-size files each (Default: 10)
    """)



def batch_process(process,
                  in_files=['.'],
                  out_dir='.',
                  batch_size=10,
                  batch_dir_prefix='batch',
                  verbosity=1):
    """
    Arguments:
        process
        in_dir
        out_dir
        batch_size
        batch_dir_prefix
    Returns:
        Nothing
    """

