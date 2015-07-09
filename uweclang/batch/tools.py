"""UWEC Language Tools batch tools module

    Provides functions for processing data in batches.
"""


def batch_process(process,
                  in_dir='.',
                  out_dir='.',
                  subdirs=True,
                  batch_size=10,
                  batch_dir_prefix='batch'):
    """
    Arguments:
        process
        in_dir
        out_dir
        subdirs
        batch_size
        batch_dir_prefix
    Returns:
        Nothing
    """

