# License: The MIT License (MIT)

# Copyright (c) 2015 Skylor R. Schermer

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

# Import all functions from the binary module:
from uweclang.binary.docx import *

# Import all functions from the plain module:
from uweclang.plain.student import *
from uweclang.plain.tools import *

# Import all functions from the tagged module:
from uweclang.tagged import *

# Import all functions from the batch module:
from uweclang.batch.tools import *
