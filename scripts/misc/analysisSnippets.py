#set up corpus

import nltk
from nltk.corpus import TaggedCorpusReader

BGSCorpus = TaggedCorpusReader("/Volumes/archive$/WOLTERLK/Summer 2015/Student Corpus/Tagged Files", ".*txt")

for f in BGSCorpus.fileids():
	print f, len([w for w in BGSCorpus.words(f) if w.isalpha()])
