"""UWEC Language Tools query module.

    This module provides tools for executing corpus queries.
"""
__author__     = 'Skylor R. Schermer'
__copyright__  = 'Copyright 2015'
__credits__    = ['Skylor R. Schermer',
                  'Victor Francisco']
__license__    = 'MIT'
__version__    = '0.1.0'
__maintainer__ = 'Skylor R. Schermer'
__email__      = 'schermsr@uwec.edu'
__status__     = 'Development' # or Production/Deprecated


__all__ = ['result', 'abstract', 'query', 'grammar']

# Setup logger.
import logging
logging.getLogger('uweclang.query').addHandler(logging.NullHandler())
