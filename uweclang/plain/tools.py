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

"""UWEC Language Tools plaintext tools module

    Provides basic functions for handling plaintext data.
"""

def line_split(text, remove_empty_lines=True, strip_lines=True, sep='\n'):
    """Splits plaintext input into lines.

    Args:
        text (str): The text to split.
        remove_empty_lines (Optional[bool]): Whether empty lines should be
            removed from the result. Defaults to True.
        strip_lines (Optional[bool]): Whether to strip whitespace from the ends
            of each line. Defaults to True.
        sep (Optional[str]): The regex to use for seperating the lines.
            Defaults to '\n'.

    Returns:
        A generator producing the lines in the text.
    """
    res = text.split(sep)

    if strip_lines:
        res = (line.strip() for line in res)

    if remove_empty_lines:
        res = (line for line in res if line)

    return res
