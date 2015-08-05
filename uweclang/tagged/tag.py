# -*- coding: utf-8 -*-
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

# Standard imports
import re
import nltk

from itertools import chain
from collections import defaultdict, Counter

_PUNCTUATION_REGEX = re.compile(r'``|\'\'|[^\w\s]')


NOMINALIZATION_SUFFIXES = {
    'tion',
    'tions',
    'ment',
    'ments',
    'ness',
    'nesses',
    'ity',
    'ities'}

BE_FORMS = {
    'am',
    'are',
    'be',
    'been',
    'being',
    'is',
    'was',
    'were'}

LINKING_ADVERBS = {
    'actually',
    'accordingly',
    'afterwards',
    'admittedly',
    'consequently',
    'eventually',
    'anyhow',
    'hence',
    'finally',
    'anyway',
    'naturally',
    'first',
    'conversely',
    'otherwise',
    'firstly',
    'however',
    'so',
    'last',
    'instead',
    'therefore',
    'lastly',
    'nevertheless',
    'thus',
    'next',
    'still',
    'second',
    'though',
    'secondly',
    'yet',
    'third',
    'thirdly'}

ADDITIVE_ADVERBS = {
    'additionally',
    'also',
    'alternatively',
    'further',
    'furthermore',
    'likewise',
    'moreover',
    'namely',
    'similarly'}

LINKING_BIGRAMS = {
    ('above', 'all'),
    ('after', 'all'),
    ('as', 'well'),
    ('by', 'comparison'),
    ('by', 'contrast'),
    ('for', 'instance'),
    ('in', 'comparison'),
    ('in', 'addition'),
    ('in', 'contrast'),
    ('that', 'is'),
    ('in', 'fact'),
    ('in', 'reality'),
    ('other', 'hand'),
    ('then', 'again')}

ADDITIVE_BIGRAMS = {
    ('for', 'instance'),
    ('for', 'example')}

LINKING_TRIGRAMS = {
    ('all', 'things', 'considered'),
    ('as', 'a', 'consequence'),
    ('as', 'a', 'result'),
    ('in', 'that', 'case')}

def tag(text):
    """Tags the input text.

    Arguments:
        text (str): The text to tag.

    Returns:
        ([[(str, str)]]): List of sentences containing lists of word/tag pairs.
    """
    #Separate the input text into sentences
    sentences = nltk.sent_tokenize(text)

    #Separate each sentence into words
    nested = []
    for sentence in sentences:
        nested.append(nltk.word_tokenize(sentence))

    #Add a part of speech tag to each word
    nested_tagged = []
    for sentence in nested:
        nested_tagged.append(nltk.pos_tag(sentence))

    return nested_tagged


def get_tags(tagged):
    """Returns a dict of all tags in the given tagged text, allong with their
    counts and word set.

    Arguments:
        tagged (str): The tagged text.

    Returns:
        (dict):
    """
    tag_dict = defaultdict(dict)
    for token, tag in chain.from_iterable(tagged):
        try:
            tag_dict[tag][token] += 1
        except KeyError:
            tag_dict[tag].update({token : 1})
    return tag_dict


def read_tagged_string(text):
    return [[nltk.tag.str2tuple(x) for x in line.split()] for line in text.split('\n')]


def tagged_to_plain(tagged):
    tagged = chain.from_iterable(tagged)
    text = ' '.join((x[0] for x in tagged))

    text = re.sub(r"`` | ''", '"', text)
    text = re.sub(r' (n\'t|\'s|[^\w\s\"\'])', r'\1', text)

    return text


def parse_tag_parentheticals(tagged, lparen='(', rparen=')', use_tag=False):
    """Parses the given text and returns a tree of parentheticals.

    Arguments:
        text (str): The input text.
        lparen (str): The left parenthetical delimiter. Defaults to '('.
        rparen (str): The right parenthetical delimiter. Defaults to ')'.
        use_tag (bool): Whether to match the delimiter against the tag or the
            text. Defaults to False (text).

    Returns:
        (dict | [(str, str)]): A dictionary representing the parse tree or a
        list of tagged tokens. Each node of the tree will have the following
        structure:

            {'parens': (l, r), 'tagged': []}

        where (l, r) are the parentheticals wrapping the text, and the list
        contains tokens and subnodes.

        Unmatched lparens will be interpretted as regular tokens. Unmatched
        rparens will have None as their second parens tuple element. If there
        are no parentheticals, a list of tagged tokens will be returned.
    """
    tagged = chain.from_iterable(tagged)

    part = 1 if use_tag else 0

    # Build root of tree.
    tree = {'parens': (None, None),
            'tagged': []}

    context = [tree]

    # Keep parsing until nothing is left.
    for item in tagged:
        node = context[0]

        # Match rparens.
        if item[part] == rparen:

            if node['parens'] == (None, None):
                node['tagged'].append(item[0])
            else:
                node = context.pop(0)
                node['parens'] = (node['parens'][0], item)

            continue

        # Match lparens.
        if item[part] == lparen:
            new_node = {'parens': (item, None),
                        'tagged': []}
            node['tagged'].append(new_node)
            context.insert(0, new_node)

            continue

        # Match text.
        node['tagged'].append(item)

    # Remove highest level tree if whole string is parenthetical.
    if len(tree['tagged']) == 1:
        tree = [tree['tagged'][0]]

    return tree


def recombine_tag_parentheticals(parse_tree, selector_function=None):
    """Recombines tagged text seperated by the seperate_tag_parentheticals function by
    using a selector function to determine which portions to keep or discard.

    Arguments:
        parse_tree (dict): A tree of parsed parentheticals
            (See parse_parentheticals.)
        selector_function ((TAG, TAG), [TAG] -> true): A function taking a pair
            of tagged parenthesis and a list of tagged tokens, and returning
            whether to keep the tokens or discard them. Allows for selective
            recombination of text. Defaults to None (everything is kept.)
            (TAG is of the form (str, str))

    Returns:
        ([(str, str)]): The resulting tagged text.

    Raises:
        (ValueError): When unkown values are contained in parse_tree.
    """
    # Set default selector test function if none is provided.
    selector_function = selector_function or (lambda x, y: True)

    # Reconstruct parse tree root for lists and strings.
    if isinstance(parse_tree, list):
        parse_tree = {'parens': (None, None), 'tagged': parse_tree}
    elif isinstance(parse_tree, tuple):
        parse_tree = {'parens': (None, None), 'tagged': [parse_tree]}

    tagged = []
    for item in parse_tree['tagged']:
        if isinstance(item, tuple):
            tagged.append(item)

        elif isinstance(item, dict):
            # Recreate text from rest of this node.
            res = recombine_tag_parentheticals(item,
                                           selector_function=selector_function)
            # Append text if it passes selector test.
            if selector_function(parse_tree['parens'], res):
                tagged.extend(res)

        else:
            raise ValueError('Unknown parse tree content.')


    # Use selector test on the whole tree.
    if selector_function(parse_tree['parens'], tagged):
        l = [parse_tree['parens'][0]]
        r = [parse_tree['parens'][1]]
        return [x for x in chain.from_iterable([l, tagged, r]) if x is not None]
    return []


def is_punctuation(word):
    if isinstance(word, tuple):
        word = word[0]
    return _PUNCTUATION_REGEX.match(word) is not None


def ngram(words, n=2):
    """Returns a generator producing the ngrams of lenght n of the input sentence.

    Arguments:
        words ([str]): A list of words.
        n (int): The length of the n-grams.

    Returns:
        [(str, str, ...)]: A list of word tuples containing nearby words in
        n-length groups.
    """
    cur = 0
    while cur < len(words)-(n-1):
        yield words[cur:cur+n]
        cur += 1

def analysis_to_str(data):
    """Converts a dictionary of analyzed file data to a formatted string for
    printing.

    Arguments:
        data (dict): The data to format.

    Returns:
        (str): A string representation of the data.
    """
    fmt = '{:30}, {:>6}, {};'
    sfmt = '\t{:26}, {:>6}, {};'
    lines = []
    for key, val in data.iteritems():
        if isinstance(val, list):
            lines.append('{}: {}'.format(key, len(val)))
            lines.extend(['\t' + i for i in val])

    for key, val in data.iteritems():
        if not isinstance(val, Counter) and not isinstance(val, list):
            lines.append(fmt.format(key, val, type(val).__name__))

    for key, val in data.iteritems():
        if isinstance(val, Counter):
            total = sum(val.values())
            lines.append(fmt.format(key, total, 'Counter'))
            for k, v in val.iteritems():
                if isinstance(k, tuple):
                    lines.append(sfmt.format(' '.join(k), v, type(v).__name__))
                else:
                    lines.append(sfmt.format(k, v, type(v).__name__))

    return '\n'.join(lines)


_CSV_ANALYSIS_HEADER_MEASURES =[
    'File',
    'Sentences (Total)',
    'Tokens (Total)',
    'Words (Total)',
    'Punc. Tokens (Total)',
    'Nouns (Total)',
    'Modified Nouns (Total)',
    'Modified Noun Ratio',
    'Nominalizations (Total)',
    'Verbs (Total)',
    'Tensed Verb Ratio',
    'Passives (Total)',
    'Passives/Verb',
    'Tags (Total)',
    'Type/Token Ratio',
    'Words/Sentence',
    'Tokens/Word',
    'Tokens/Sentence',
    ]

# Build CSV Header row from column data.
CSV_ANALYSIS_HEADER = (_CSV_ANALYSIS_HEADER_MEASURES +
                       list(NOMINALIZATION_SUFFIXES) +
                       list(ADDITIVE_ADVERBS) +
                       [' '.join(x) for x in ADDITIVE_BIGRAMS] +
                       list(LINKING_ADVERBS) +
                       [' '.join(x) for x in LINKING_BIGRAMS] +
                       [' '.join(x) for x in LINKING_TRIGRAMS])

def get_csv_data(data):
    """Converts a dictionary of analyzed file data to a list of CSV row
    entries.

    Arguments:
        data (dict): The data to format.

    """
    row = dict()

    # Note: The iteration order in these loops must match that of the
    # CSV_ANALYSIS_HEADER. Do not add/re-order items in the header and expect
    # this function to work on old data!
    for item in _CSV_ANALYSIS_HEADER_MEASURES:
        row[item] = data[item]

    for item in NOMINALIZATION_SUFFIXES:
        row[item] = data['Nominalizations'].get(item, 0)

    for item in ADDITIVE_ADVERBS:
        row[item] = data['Additive Adverbs'].get(item, 0)

    for item in [' '.join(x) for x in ADDITIVE_BIGRAMS]:
        row[item] = data['Additive Adverbs'].get(item, 0)

    for item in LINKING_ADVERBS:
        row[item] = data['Linking Adverbs'].get(item, 0)

    for item in [' '.join(x) for x in LINKING_BIGRAMS]:
        row[item] = data['Linking Adverbs'].get(item, 0)

    for item in [' '.join(x) for x in LINKING_TRIGRAMS]:
        row[item] = data['Linking Adverbs'].get(item, 0)

    return row
