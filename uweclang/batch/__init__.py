"""UWEC Language Tools batch module.

    This module provide tools for processing files in batches.
"""
__author__     = 'Skylor R. Schermer'
__copyright__  = 'Copyright 2015'
__credits__    = ['Skylor R. Schermer']
__license__    = 'MIT'
__version__    = '0.1.0'
__maintainer__ = 'Skylor R. Schermer'
__email__      = 'schermsr@uwec.edu'
__status__     = 'Development' # or Production/Deprecated


__all__ = ['batch']

# Setup logger.
import logging
logging.getLogger('uweclang.batch').addHandler(logging.NullHandler())
