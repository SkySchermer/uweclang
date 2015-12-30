from django.core.cache import cache


import sys
import os
sys.path.append(os.path.dirname(os.path.realpath('..')))
import uweclang
from . import settings
import logging
import pickle

log = logging.getLogger(__name__)

# _CORPUS_LOCATION = os.path.dirname(os.path.realpath('../../test/corpus'),)
_CORPUS_LOCATION = r'/Volumes/archive$/WOLTERLK/Summer 2015/Student Corpus/'
_CORPUS_CACHE = '.cached.corpus'

# Load corpus.
corpus = None
if os.path.isfile(_CORPUS_CACHE):
    try:
        with open(_CORPUS_CACHE, 'rb') as corpus_file:
            log.info('Loading corpus... ')
            corpus = pickle.load(corpus_file)
            log.info('Done. ({} files identified)'.format(corpus.file_count))
    except EOFError:
        log.info('Unable to find corpus cache.')
        pass

# Setup Corpus
if not corpus:
    log.info('Initializing corpus... ')
    sys.stdout.flush()
    old_dir = os.getcwd()
    os.chdir(_CORPUS_LOCATION)
    # Build corpus.
    corpus = uweclang.StudentCorpus(search_locations='.', recursive=True)
    os.chdir(old_dir)
    log.info('{} files added ({} words)'.format(
        corpus.file_count,
        corpus.word_count))

    with open(_CORPUS_CACHE, 'w') as corpus_file:
        pickle.dump(corpus, corpus_file, pickle.HIGHEST_PROTOCOL)


cache.set('corpus', corpus)
