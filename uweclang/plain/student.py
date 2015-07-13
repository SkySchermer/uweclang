# -*- coding: utf-8 -*-
"""UWEC Language Tools student corpus module

    Provides functions for processing student corpus data.
"""
import re

def punctuation_density(text, punctuation=r'[^\w\s]'):
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

    words = re.sub(r'\W', ' ', text).split()
    puncs = float(sum([len(re.findall(punctuation, x)) for x in text]))

    return (puncs / len(words)) if len(words) > 0 else 0.0


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

    words = re.sub(r'\W', ' ', text).split()
    caps = float(sum([1 for x in words if re.match('[A-Z]', x)]))

    return (caps / len(words)) if len(words) > 0 else 0.0


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
        (dict | [str]): A dictionary representing the parse tree or a list of
        strings. Each node of the tree will have the following structure:

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
        rparens will have None as their second parens tuple element. If there
        are no parentheticals, a list of text will be returned.

    """
    # Precompile regular expressions for ease of use.
    n_regex = re.compile(r'([^{}{}]*)'.format(lparen, rparen))
    l_regex = re.compile(r'({})'.format(lparen))
    r_regex = re.compile(r'({})'.format(rparen))

    # Build root of tree.
    tree = {'parens': (None, None),
            'text': []}

    context = [tree]
    rest = text

    # Keep parsing until nothing is left.
    while rest:
        node = context[0]

        # Match rparens.
        m = r_regex.match(rest)
        if m:
            if node['parens'] == (None, None):
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
        tree = [tree['text'][0]]

    return tree


def recombine_parentheticals(parse_tree, selector_function=None, sep=''):
    """Recombines text seperated by the seperate_parentheticals function by
    using a selector function to determine which portions to keep or discard.

    Arguments:
        parse_tree (dict): A tree of parsed parentheticals
            (See parse_parentheticals.)
        selector_function ((str, str), str -> true): A function taking a pair
            of parenthesis and a string, and returning whether to keep the
            string or discard it. Allows for selective recombination of text.
            Defaults to None (everything is kept.)
        sep (str): The seperator to use when combining the text. Defaults to
            ''.

    Returns:
        (str): The resulting text.

    Raises:
        (ValueError): When unkown values are contained in parse_tree.
    """
    # Set default selector test function if none is provided.
    selector_function = selector_function or (lambda x, y: True)

    # Reconstruct parse tree root for lists and strings.
    if isinstance(parse_tree, list):
        parse_tree = {'parens': (None, None), 'text': parse_tree}
    elif isinstance(parse_tree, str):
        parse_tree = {'parens': (None, None), 'text': [parse_tree]}

    text = []
    for item in parse_tree['text']:
        if isinstance(item, str):
            text.append(item)

        elif isinstance(item, dict):
            # Recreate text from rest of this node.
            res = recombine_parentheticals(item,
                                           selector_function=selector_function,
                                           sep=sep)
            # Append text if it passes selector test.
            if selector_function(parse_tree['parens'], res):
                text.append(res)

        else:
            raise ValueError('Unknown parse tree content.')


    res = sep.join(text)
    # Use selector test on the whole tree.
    if selector_function(parse_tree['parens'], res):
        l = parse_tree['parens'][0]
        r = parse_tree['parens'][1]
        return sep.join([x for x in [l, res, r] if x is not None])
    return ''



