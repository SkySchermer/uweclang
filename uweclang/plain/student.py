"""UWEC Language Tools student corpus module

    Provides functions for processing student corpus data.
"""
import re

def punctuation_density(text, punctuation=r'[,.!?:;\\/]'):
    '''Returns the punctuation density of the given text.

    Arguments:
        text (str): The input text.
        punctuation (str): A regex pattern for matching punctuation characters.
            Defaults to r'[,.!?:;\\/]'.
    Returns:
        (float): The density of puntuation in the text.
    '''
    if len(text) == 0:
        return 0

    return len(re.findall(punctuation, text)) / len(text)


def capitalization_density(text):
    '''Returns the word-starting capitalized character density of the given
    text.

    Arguments:
        text (str): The input text.

    Returns:
        (float): The density of capitalized words in the text.
    '''
    if len(text) == 0:
        return 0

    return len(re.findall(r'\b[A-Z]\w+', text)) / len(text)


def straighten_quotes(text):
    '''Returns the text with angled quotes replaced with straight quotes.

    Arguments:
        text (str): The input text.

    Returns:
        (str) The modified text.
    '''

    text = re.sub(r'[“”]', '', text)
    text = re.sub(r'[‘’]', '', text)

    return text


def remove_punctuation_spaces(text, punctuation=',.!?:;'):
    '''Returns text modified by removing whitespace before punctuation.

    Arguments:
        text (str): The input text.
        punctuation (str): string containing the punctuation to remove
            whitespace before. Defaults to ',.!?:;'.

    Returns:
        (str): The modified text.
    '''
    for char in punctuation:
        text = re.sub(r'\b\s+{}'.format(char), char, text)

    return text


def seperate_parentheticals(text, lparen='\(', rparen='\)'):
    '''Returns the text split into a list of parenthetical and
    non-parenthetical text.

    It is important to remember to escape the parentheticals if the have a
    meaning in regex.

    Arguments:
        text (str): The input text.
        lparen (str): The regex of the left parenthetical. Defaults to '\('.
        rparen (str): The regex of the right parenthetical. Defaults to '\)'.

    Returns:
        ([(str, bool)]): A generator of tuples containing the text and whether or
            not the text was in a parenthetical.
    '''
    def tuplify(x):
        if x[0] == '\x1e':
            return (x[1:], True)
        return (x, False)

    # This substitution is a little complicated. We want to match '<([^>])>',
    # where the <, > characters are our parentheticals, and the middle part is
    # captured as a group. We use the alternation '|' to ensure that we can
    # match an empty string in the middle.
    #
    # In the second argument, we wrap the captured group in special characters
    # (the ASCII 'group seperator' special code \x1d), and we prefix it with
    # a different code (the ASCII 'record seperator' special code \x1e). These
    # codes are used to split the text and identify what parts were
    # parenthetical and which were not.
    text = re.sub(r'{0}([^{1}]+|){1}'.format(lparen, rparen),
                  '\x1d\x1e\\1\x1d',
                  text)

    return (tuplify(x) for x in text.split('\x1d') if x)

