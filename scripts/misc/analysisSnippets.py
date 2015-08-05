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

BGSCorpus = TaggedCorpusReader("/Volumes/archive$/WOLTERLK/Summer 2015/Student Corpus/Tagged Files", ".*txt")




"""
Loop through each file and print a wordcount, excluding punctuation. Running just this much
is an easy way to check for empty files, which will render the corpus unusable.
"""


for f in BGSCorpus.fileids():
	print f, len([w for w in BGSCorpus.words(f) if w.isalpha()])
	


"""
Calculate type-to-token ratio of first 500 words
"""

"""
for f in BGSCorpus.fileids():
	words = [w.lower() for w in BGSCorpus.words(f) if w.isalpha()]
	if len(words)>499:
		TTR = len(set(words[0:499]))/500.0
		print f, TTR
"""


"""
Count nominalizations (with redundant wordcount)
Linguistics note: we're actually counting words that end in -tion(s), -ness(es), -ment(s), -ity
and -ities, which will include some words that are not derived nouns (such as "city"
or "notion").

Optional coding extension: instead of returning raw counts by suffix, calculate nominalizations
per million words as follows:
sum all nominalizations in the file, divide by wordcount of file, multiply by 1,000,000

"""

"""
suffixes = ['tion', 'tions', 'ment', 'ments', 'ness', 'nesses', 'ity', 'ities']

print "file wordcount tion tions ment ments ness nesses ity ities"

for f in BGSCorpus.fileids():
	print f,
	print len([w for w in BGSCorpus.words(f) if w.isalpha()]),
	for suffix in suffixes:
		print len([w for w in BGSCorpus.words(f) if w.endswith(suffix)]),
	print " "
"""

"""
Calculate the percentage of finite verbs (ignoring modals) that are present tense.

"""

"""
print 'file percent-present'

for f in BGSCorpus.fileids():
	present = len([w for (w,t) in BGSCorpus.tagged_words(f) if (t=='VBP' or t=='VBZ')])
	past = len([w for (w,t) in BGSCorpus.tagged_words(f) if t=='VBD'])
	print f, float(present)/float(present+past)*100
"""

"""
Estimate what percent of clauses are in passive voice.

1. Estimate the number of tensed clauses by counting tensed verbs and modals, because each
clause contains exactly one tensed verb or modal. Linguistics note: ideally we should be counting
nonfinite clauses as well. If we can figure out a way to distinguish auxiliaries from main
verbs (which is not done in the Penn treebank tagset), we can count main verbs instead of 
finite verbs and modals.

2. Estimate the number of passive clauses by looking for this sequence: form of BE - optional
extra word - past participle. Linguistics note: sometimes an adverb, e.g. also, is inserted
between passive be and the past participle. Possibly worth exploring the corpus to find out
whether more than one word can occur in this position.

"""

"""
beForms = ['am', 'are', 'be', 'been', 'being', 'is', 'was', 'were']

print 'file verbs passives percent'

for f in BGSCorpus.fileids():
	countVerbs = len([(w,t) for (w,t) in BGSCorpus.tagged_words(f) if (t=='MD' or t=='VBD' or t=='VBP' or t=='VBZ')])
	countPassives = len([w3 for (w1, t1), (w2, t2), (w3,t3) in nltk.trigrams(BGSCorpus.tagged_words(f)) 
	if w1.lower() in beForms and (t2=='VBN' or t3=='VBN')])
	print f, countVerbs, countPassives, float(countPassives)/float(countVerbs)*100	
"""


"""
Count total nouns and adjective-noun sequences.

Linguistics note: first pass at considering what proportion of nouns are modified.

"""

"""
print 'file nouns A-N'

for f in BGSCorpus.fileids():
	countN = len([(w,t) for (w,t) in BGSCorpus.tagged_words(f) if t != None and t.startswith('NN')])
	countAN = len([w1 for (w1,t1),(w2,t2) in nltk.bigrams(BGSCorpus.tagged_words(f)) if 
	t1 != None and t2 != None and t1.startswith('JJ') and t2.startswith('NN')])
	print f, countN, countAN
"""
