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
