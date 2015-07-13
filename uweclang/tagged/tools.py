# -*- coding: utf-8 -*-
import nltk

class TaggedText:
    """ 
    """
    def __init__(self, text, do_tagging=False):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def parse_parentheticals(self):
        pass

    def recombine_parentheticals(self):
        pass

    def getTags(self):
        pass

    def count_tags(self, tag_regex=None):
        pass


def tag(text):
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

