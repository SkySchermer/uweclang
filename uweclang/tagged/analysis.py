# -*- coding: utf-8 -*-
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

# Standard imports
import re

from itertools import chain
from collections import defaultdict, Counter
from uweclang import TaggedToken

# Setup logger.
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

_PUNCTUATION_REGEX = re.compile(r'``|\'\'|[^\w\s]')

DATE_REGEX_MDY = re.compile(r"""
    (1[012]|0\d|\d)
    \ ?/\ ?
    (3[01]|[012]\d|\d)
    \ ?/\ ?
    (\d{2,4})?
    """, re.VERBOSE)

DATE_REGEX_DMY = re.compile(r"""
    (3[01]|[012]\d|\d)?
    \ ?/\ ?
    (1[012]|0\d|\d)
    \ ?/\ ?
    (\d{2,4})?
    """, re.VERBOSE)

DATE_REGEX_DMONY = re.compile(r"""
    (3[01]|[012]\d|\d)?
    \ ?
    (jan(?:uary)?
    |feb(?:ruary)?
    |mar(?:ch)?
    |apr(?:il)?
    |may
    |jun(?:e)?
    |jul(?:y)?
    |aug(?:ust)?
    |sep(?:tember)?
    |oct(?:ober)?
    |nov(?:ember)?
    |dec(?:ember)?)
    \ ?
    (\d{2,4})?
    """, re.IGNORECASE | re.VERBOSE)

DATE_REGEX_MONDY = re.compile(r"""
    (jan(?:uary)?
    |feb(?:ruary)?
    |mar(?:ch)?
    |apr(?:il)?
    |may
    |jun(?:e)?
    |jul(?:y)?
    |aug(?:ust)?
    |sep(?:tember)?
    |oct(?:ober)?
    |nov(?:ember)?
    |dec(?:ember)?)
    \ ?
    (3[01]|[012]\d|\d)
    (,\ ?\d{2,4})?
    """, re.IGNORECASE | re.VERBOSE)

DATE_REGEX_ANY = re.compile('(?:' + DATE_REGEX_DMY.pattern + ')|' +
                            '(?:' + DATE_REGEX_MDY.pattern + ')|' +
                            '(?:' + DATE_REGEX_DMONY.pattern + ')|' +
                            '(?:' + DATE_REGEX_MONDY.pattern + ')',
                            re.IGNORECASE | re.VERBOSE)

DATE_REGEX_ANY_FULL = re.compile('^' + DATE_REGEX_ANY.pattern + '$', re.IGNORECASE | re.VERBOSE)

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


def is_punctuation(word):
    if isinstance(word, TaggedToken):
        word = word.token
    return _PUNCTUATION_REGEX.match(word) is not None


def analysis_to_str(data):
    """Converts a dictionary of analyzed file data to a formatted string for
    printing.

    Arguments:
        data (dict): The data to format.

    Returns:
        (str): A string representation of the data.
    """
    fmt = '{:32}, {:>15}, {};'
    sfmt = '\t{:28}, {:>15}, {};'
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

            # Get values in Counter. We sort the values by -count, then by key
            # name
            for k, v in ((k, val[k]) for k in sorted(val,
                                                     key=lambda x: (-val[x], x))):
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

    Returns:
        (list): A list of CSV columns for the given data.

    Use CSV_ANALYSIS_HEADER to get a header for the data produced by this
    function.

    """
    row = dict()

    # Note: The iteration order in these loops must match that of the
    # CSV_ANALYSIS_HEADER. Do not add/re-order items in the header and expect
    # this function to work on old data!
    for item in _CSV_ANALYSIS_HEADER_MEASURES:
        row[item] = data[item]

    for item in NOMINALIZATION_SUFFIXES:
        row[item] = data['Nominalizations'].get(item, None)

    for item in ADDITIVE_ADVERBS:
        row[item] = data['Additive Adverbs'].get(item, None)

    for item in (' '.join(x) for x in ADDITIVE_BIGRAMS):
        row[item] = data['Additive Adverbs'].get(item, None)

    for item in LINKING_ADVERBS:
        row[item] = data['Linking Adverbs'].get(item, None)

    for item in (' '.join(x) for x in LINKING_BIGRAMS):
        row[item] = data['Linking Adverbs'].get(item, None)

    for item in (' '.join(x) for x in LINKING_TRIGRAMS):
        row[item] = data['Linking Adverbs'].get(item, None)

    return row

def calculate_type_token(tokens):
    return (len(set((x[0] for x in tokens))),
            len(set((x[1] for x in tokens))))

def calculate_type_token_ratio(tokens):
    type_c, token_c = calculate_type_token(tokens)
    return type_c / token_c if token_c != 0 else 0
