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
                          dest='extra_files',
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
    batch the output into subdirectories. The batch-size parameter is used
    together with the --batch-mode option to determine how many subdirectories
    or files per subdirectories to use.
    """)

BATCH_PARSER.add_argument('-m', '--batch-mode',
                          nargs='?',
                          choices=['count', 'divide'],
                          default='count',
                          metavar='mode',
                          dest='batch_mode',
                          help="""
    sets the batch mode. In count mode, each batch will contain at most the
    number of files specified by the --batch argument (default 10). In divide
    mode, there will be that number of batch directories, and files will be
    divided evenly between them.
    """)


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

    # Process files:
    # for filename in single_files:
    #     name_part = os.path.splitext(path)[0]
    #     extract_plaintext_from_docx(filename,
    #                                 os.path.join(out_path, name_part + args.oext),
    #                                 verbosity=args.verbose)

