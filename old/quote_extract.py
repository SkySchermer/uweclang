#! /usr/bin/env python3

import sys
import nltk
import re

from nltk.corpus import PlaintextCorpusReader

def get_tag(word_with_tag):
    spl = word_with_tag.split('/')

    if len(spl) == 2:
        return (spl[0], spl[1])
    else:
        return (spl[0], None)

def remove_empty(items):
    return [item for item in items if item]


def nnp_density(words):
    if not words:
        return 0

    count = len(words)
    proper_noun_count = 0
    for word in words:
        if word[1] and word[1].startswith('NNP'):
            proper_noun_count += 1

    return float(proper_noun_count)/count

def reassemble(tagged):
    words = []
    for w_tag in tagged:
        if w_tag[1] == '``':
            words.append('“')
        elif w_tag[1] == "''":
            words.append('”')
        elif w_tag[1]:
            words.append(str(w_tag[0]) + '/' + str(w_tag[1]))
    return ' '.join(words)

def get_quotes(raw_text):
    quotes = []
    lines = [x.split(' ') for x in raw_text.split('\n')]
    lines = map(remove_empty, lines)

    for sentence in lines:
        tagged = list(map(get_tag, sentence))

        result = reassemble(tagged)

        for quote in re.findall(r'[“”][^“”]*[“”]', result):
            tagged_quote = list(map(get_tag, quote.split(' ')))
            quotes.append([item for item in tagged_quote if item[1]])
    return quotes

if __name__ == '__main__':

    if len(sys.argv) < 2:
        directory = '.'
    else:
        directory = sys.argv[1]


    myCorpus = PlaintextCorpusReader(directory, '.*.txt')


    for fileid in myCorpus.fileids():
        raw_text = myCorpus.raw(fileid)
        num_chars = len(myCorpus.raw(fileid))
        words = myCorpus.words(fileid)
        num_vocab = len(set([w.lower() for w in myCorpus.words(fileid)]))
        av_wordlength = (num_chars / len(words)) - 1
        lex_diversity = float(num_vocab) / len(words)
        print('{}: \tWC: {} \tAVG_WLEN: {:.3f} \tDIV: {:.3f}'.format(fileid,
              len(words),
              av_wordlength,
              lex_diversity))

        quotes = get_quotes(raw_text)
        for line in quotes:
            print('\t', len(line), ' '.join([x[0] for x in line])[:70])

        if quotes:
            print('\tAVG quote length:', float(sum(map(len, quotes))) / len(quotes))



