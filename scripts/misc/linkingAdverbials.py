"""
set up corpus

TaggedCorpusReader takes two arguments:
1. which directory to consider
2. which files from that directory to include

If you want to test something with the Summer 2014 pilot corpus (stable & much smaller),
change first argument to "/Volumes/archive$/WOLTERLK/PilotCorpus2014/Tagged"

TaggedCorpusReader general info

corpusname.fileids()		list of filenames in corpus
corpusname.words() 			list of words, including punctuation.
corpusname.tagged_words() 	list of (word, tag) pairs.
corpusname.sents() 			list of sentences, each of which is a list of words.
corpusname.tagged_sents() 	list of sentences, each of which is a list of (word, tag) pairs.

All of the above except fileids take a filename as an optional argument.

"""

import nltk
from nltk.corpus import TaggedCorpusReader

BGSCorpus = TaggedCorpusReader("/Volumes/archive$/WOLTERLK/Summer 2015/Student Corpus/Tagged Files", "120.*txt")


"""
One option for counting individual words: Construct a separate count for each word of interest.
Code below prints counts for a short list of words and an arbitrary file
"""

"""
additiveAdverbs = ['additionally', 'also', 'alternatively', 'further', 'furthermore', 'likewise', 'moreover', 'namely', 'similarly']


for target in additiveAdverbs:
	print len([w for w in BGSCorpus.words('120-S15-6773086.tag.txt') if w.lower()==target])
"""

"""
A similar option for counting bigrams (and trigrams): Construct a separate count for each ngram of interest.
Code below prints counts of two bigrams for an arbitrary file
"""

"""
additiveBigrams = [('for','instance'),('for','example')]

for target in additiveBigrams:
	print len([(w1,w2) for (w1,w2) in nltk.bigrams(BGSCorpus.words('120-S15-6773086.tag.txt')) if w1.lower()==target[0] and w2.lower()==target[1]])
"""


"""
Another option for counting individual words: First, construct a frequency distribution for a file (which tabulates
the number of occurrences of each word type). Then retrieve the counts for words of interest.
"""

"""
additiveAdverbs = ['additionally', 'also', 'alternatively', 'further', 'furthermore', 'likewise', 'moreover', 'namely', 'similarly']

from nltk.probability import FreqDist

fd = FreqDist(w.lower() for w in BGSCorpus.words('120-S15-6773086.tag.txt'))

for target in additiveAdverbs:
	print fd[target]
"""

"""
It's also possible to build a frequency distribution of bigrams (or trigrams), as below

"""

"""
additiveBigrams = [('for','instance'),('for','example')]

from nltk.probability import FreqDist

bigramFrequencies = FreqDist((w1.lower(),w2.lower()) for (w1,w2) in nltk.bigrams(BGSCorpus.words('120-S15-6773086.tag.txt')))

for target in additiveBigrams:
	print bigramFrequencies[target]
"""	

"""
If you want to start by constructing frequency distributions for all of files (then retrieve data about
particular files as needed), a conditional frequency distribution (ConditionalFreqDist) might be useful.
"""