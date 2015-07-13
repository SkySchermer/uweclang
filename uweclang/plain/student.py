# -*- coding: utf-8 -*-
"""UWEC Language Tools student corpus module

    Provides functions for processing student corpus data.
"""
import re

def punctuation_density(text, punctuation=r'[,.!?:;\\/]'):
    """Returns the punctuation density of the given text.

    Arguments:
        text (str): The input text.
        punctuation (str): A regex pattern for matching punctuation characters.
            Defaults to r'[,.!?:;\\/]'.
    Returns:
        (float): The density of puntuation in the text.
    """
    if len(text) == 0:
        return 0

    return len(re.findall(punctuation, text)) / len(re.findall(r'\b\w+', text))


def capitalization_density(text):
    """Returns the word-starting capitalized character density of the given
    text.

    Arguments:
        text (str): The input text.

    Returns:
        (float): The density of capitalized words in the text.
    """
    if len(text) == 0:
        return 0

    text = re.sub('\W', ' ', text)
    return len(re.findall(r'\b[A-Z]\w+', text)) / len(re.findall(r'\b\w+', text))


def straighten_quotes(text):
    """Returns the text with angled quotes replaced with straight quotes.

    Arguments:
        text (str): The input text.

    Returns:
        (str) The modified text.
    """

    text = re.sub(r'[“”]', '', text)
    text = re.sub(r'[‘’]', '', text)

    return text


def remove_punctuation_spaces(text, punctuation=',.!?:;'):
    """Returns text modified by removing whitespace before punctuation.

    Arguments:
        text (str): The input text.
        punctuation (str): string containing the punctuation to remove
            whitespace before. Defaults to ',.!?:;'.

    Returns:
        (str): The modified text.
    """
    for char in punctuation:
        text = re.sub(r'\b\s+{}'.format(char), char, text)

    return text


def parse_parentheticals(text, lparen='\(', rparen='\)'):
    """Parses the given text and returns a tree of parentheticals.

    Arguments:
        text (str): The input text.
        lparen (str): A regex for matching the left parenthetical delimiter.
        rparen (str): A regex for matching the right parenthetical delimiter.

    Returns:
        (dict): A dictionary representing the parse tree. Each node of the
        tree will have the following structure:

            {'parens': (l, r), 'text': []}

        where (l, r) are the parentheticals wrapping the text, and the list
        contains raw text and subnodes. For example, the following string

            'ab)c((d)ef)g()(hi'

        will return:

            {'parens': None,
             'text': ['ab',
                      ')',
                      'c',
                      {'parens': ('(', ')'),
                       'text': [{'parens': ('(', ')'), 'text': ['d']}, 'ef']},
                      'g',
                      {'parens': ('(', ')'), 'text': []},
                      {'parens': ('(', None), 'text': ['hi']}]}

        Unmatched lparens will be interpretted as regular text. Unmatched
        rparens will have None as their second parens tuple element.

    """
    n_regex = re.compile(r'([^{}{}]*)'.format(lparen, rparen))
    l_regex = re.compile(r'({})'.format(lparen))
    r_regex = re.compile(r'({})'.format(rparen))

    tree = {'parens': None,
            'text': []}
    context = [tree]
    depth = 0
    rest = text

    # Keep parsing until nothing is left.
    while rest:
        node = context[0]

        # Match rparens.
        m = r_regex.match(rest)
        if m:
            if node['parens'] is None:
                node['text'].append(m.group(1))
            else:
                node = context.pop(0)
                node['parens'] = (node['parens'][0], m.group(1))

            rest = rest[len(m.group(1)):]
            continue

        # Match lparens.
        m = l_regex.match(rest)
        if m:
            new_node = {'parens': (m.group(1), None),
                                'text': []}
            node['text'].append(new_node)
            context.insert(0, new_node)

            rest = rest[len(m.group(1)):]
            continue

        # Match text.
        m = n_regex.match(rest)
        if m:
            node['text'].append(m.group(1))

            rest = rest[len(m.group(1)):]

    # Remove highest level tree if whole string is parenthetical.
    if len(tree['text']) == 1:
        tree = tree['text'][0]

    return tree


def seperate_parentheticals(text, lparen='\(', rparen='\)'):
    """Returns the text split into a list of parenthetical and
    non-parenthetical text.

    This function is not suitable for processing nested parentheticals.

    Arguments:
        text (str): The input text.
        lparen (str): The regex of the left parenthetical. Defaults to '\('.
        rparen (str): The regex of the right parenthetical. Defaults to '\)'.

        (It is important to remember to escape the parenthetical arguments if
        theyhave a meaning in regex.)

    Returns:
        ([(str, bool)]): A generator of tuples containing the text and whether
            or not the text was in a parenthetical.

    Simple example:

        >>> list(seperate_parentheticals('ab(c)()de'))
        [('ab', False), ('c', True), ('', True), ('de', False)]
    """
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


def recombine_selected(selector_function, seperated_text, sep=''):
    """Recombines text seperated by the seperate_parentheticals function by
    using a selector function to determine which portions to keep or discard.

    Arguments:
        seperated_text ([(str, bool)]): A list of tuples containing text and a
            data value.
        selector_function (str, bool -> bool): A function taking the text and
            data value and returning whether or not to keep the text.
        sep (str): The seperator to use when combining the text. Defaults to ''.

    Returns:
        (str): The resulting text.
    """
    return sep.join([x[0] for x in seperated_text if selector_function(*x)])
