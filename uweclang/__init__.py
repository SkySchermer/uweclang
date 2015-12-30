"""UWEC language tools package.

This package provides supplemental tools for automated processing of student
corpora. It is intended to supplement NLTK.

Usage:
    The simplest way to use the package to to do a top-level import:

        import uweclang

    This will expose all of the packages attributes under the uweclang
    namespace. E.g., instead of writing

        uweclang.plain.tools.line_split()

    you can use:

        uweclang.line_split()

    The submodules can also be imported using from-import:

        from uweclang.plain.tools import line_split()

Package Layout:
    uweclang
        binary  - Tools for processing binary file formats.
        plain   - Tools for processing plaintext file formats.
        tagged  - Tools for processing tagged file formats.


See also:
    NLTK website -- http://www.nltk.org/
    NLTK book -- http://www.nltk.org/book/
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

# Setup default logger.
import logging
logging.getLogger('uweclang').addHandler(logging.NullHandler())

# Import all functions from the binary module:
from uweclang.binary.docx import *

# Import all functions from the plain module:
from uweclang.plain.plain import *
from uweclang.plain.clean import *

# Import all functions from the tagged module:
from uweclang.tagged.tag import *
from uweclang.tagged.analysis import *

# Import all functions from the batch module:
from uweclang.batch.batch import *

# Import all functions from the query module:
from uweclang.query.query import *
from uweclang.query.result import *
from uweclang.query.abstract import *
from uweclang.query.grammar import *

# Import all functions from the corpus module:
from uweclang.corpus.manager import *
from uweclang.corpus.student import *
