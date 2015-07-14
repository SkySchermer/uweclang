# -*- coding: utf-8 -*-
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

# Standard imports
import nltk
from collections import defaultdict

class TaggedText:
    """ 
    """
    nested_tagged = []
    tags = defaultdict(set)

    def __init__(self, text):
        self.nested_tagged = _tag(text)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def parse_parentheticals(self):
        pass

    def recombine_parentheticals(self):
        pass

    def originalText(self):
        text = []
        for sentence in self.nested_tagged:
            for token, tag in sentence:
                if token not in {'``', "''", '.', ','}:
                    text.append(' ')
                text.append(token)


        return ''.join(text)

    def getTags(self):
        for sentence in self.nested_tagged:
            for token, tag in sentence:
                self.tags[tag].add(token)
        return self.tags

    def count_tags(self, tag_regex=None):
        pass


def _tag(text):
    """
    """
    #Separate the input text into sentences
    sentences = nltk.sent_tokenize(text)
    print(sentences)

    #Separate each sentence into words
    nested = []
    for sentence in sentences:
        nested.append(nltk.word_tokenize(sentence))

    print(nested)
    #Add a part of speech tag to each word
    nested_tagged = []
    for sentence in nested:
        nested_tagged.append(nltk.pos_tag(sentence))

    return nested_tagged

