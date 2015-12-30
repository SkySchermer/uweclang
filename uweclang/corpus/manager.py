"""UWEC Language Tools manager module

    Provides functions for defining and managing a corpus.
"""
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import os
import hashlib
import uweclang.batch
from itertools import chain

# Import async module.
import trollius as asyncio
from trollius import From

# Setup logger.
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


def _default_filter(meta_data):
    """The default meta data filter which accepts all files. """
    return True


def default_metadata_function(filename):
    """A function producing a dictionary of metadata for a given file. This
    is the default implementation producing the file name, location, extension,
    and file size.

    Arguments:
        filename (str): The name of the file.

    Returns:
        None: If the file path is invalid.
        (dict): A dictionary containing the metadata.
    """
    if not (filename and os.path.isfile(filename)):
        return None

    metadata = dict()

    # Collect basic metadata:
    metadata['filename'] = os.path.basename(filename)
    metadata['location'] = os.path.abspath(filename)
    ext = uweclang.split_ext(filename)
    metadata['base'] = ext[0]
    metadata['extension'] = ext[1]
    metadata['size'] = os.path.getsize(filename)

    # Get word count:
    # with open(os.path.abspath(filename), 'r') as f:
    #     words = 0
    #     buf_size = 1024 * 1024
    #     read_f = f.read # loop optimization

    #     buf = read_f(buf_size)
    #     while buf:
    #         try:
    #             words += buf.count('/')
    #             buf = read_f(buf_size)
    #         except UnicodeDecodeError as e:
    #             pass # Skip decode error?
    metadata['word_count'] = 0#words

    return metadata


def get_file_md5(filename):
    """Returns the MD5 hash of the given file.
    """
    block_size = 65536
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(block_size)
    return hasher.hexdigest()


class Corpus(object):
    """A corpus object for managing a collection of tagged text files.

    Attributes:
        file_metadata (dict): A dictionary containing corpus meta data for
            files indexed by ID.
    """
    def __init__(self,
                 search_locations=[],
                 extensions=None,
                 recursive=False,
                 meta_op=default_metadata_function):
        # Save metadata function.
        self._meta_op = meta_op
        self.file_metadata = dict()
        self._current_id = 0
        self._file_count = 0
        self._word_count = 0

        self.add_files(search_locations,
                       extensions=extensions,
                       recursive=recursive)


    def add_files(self,
                  search_locations,
                  extensions=None,
                  recursive=False):
        """Searches for files in the given locations and adds them to the
        corpus.

        Arguments:
            search_locations ([str]): A list of files and directories to search.
            extensions ([str]): The file extensions to find in directories.
                Defaults to None, which will find all files.
            recursive: (bool): Whether to search directories recursively.

        Note: Files given in search_locations that do not have the specified
            extensions will be included in the output. The extensions argument
            only effects files in the directories given.
        """
        log = logging.getLogger('uweclang.corpus.manager')
        files = uweclang.get_files(search_locations,
                                   extensions=extensions,
                                   recursive=recursive)

        self._file_count += files[1]

        for f in files[0]:
            log.debug('Adding file %s', str(f))
            # Get file meta data:
            self.file_metadata[self._current_id] = self._meta_op(f)
            meta = self.file_metadata[self._current_id]
            meta['corpus_id'] = self._current_id
            # meta['MD5'] = get_file_md5(f)
            # Get file count:
            self._word_count += meta['word_count']
            # Set next file ID:
            self._current_id += 1


        # Log File add.
        log.info('Adding %s files to corpus.', self._file_count)

    @property
    def word_count(self):
        return self._word_count

    @property
    def file_count(self):
        return self._file_count

    def get_file_ids(self, predicate=None):
        """Returns a list of file ids in the corpus.

        Arguments:
            predicate (dict -> bool): A predicate for selecting files based on
                metadata. Only file ids satisfying the predicate will be
                returned.
        """
        if predicate:
            return (k for k in self.file_metadata.keys()
                        if predicate(file_metadata[k]))
        else:
            return self.file_metadata.keys()


    def get_file_text(self, file_id):
        """Returns the tagged text of the file given by its ID."""
        if not self.file_metadata.get(file_id):
            return None

        with open(self.file_metadata[file_id]['location'], 'r') as f:
            return f.read()


    def file_modified(self, file_id):
        """Returns true if the file's MD5 hash has changes since it was added
        to the corpus.
        """
        if not self.file_metadata.get(file_id):
            return None

        md5 = get_file_md5(self.file_metadata[file_id]['location'])
        return md5 != self.file_metadata[file_id]['MD5']


    def get_file_metadata(self, file_id):
        """Returns the text of the file associated with the given file_id."""
        return self.file_metadata.get(file_id)


    def get_id_for_file(self, filename):
        """Returns the id of the given file in the corpus or None if it is not
        present.
        """
        for k, v in self.file_metadata.items():
            if v['location'] == os.path.abspath(filename):
                return k
        return None


    def files(self, meta_filter=None, exclude_modified=False):
        """Returns an iterator over the metadata and text of each file in the
        corpus.
        """
        meta_filter = meta_filter or _default_filter
        for x in self.get_file_ids():
            if (meta_filter(self.get_file_metadata(x))
                and not (exclude_modified and self.file_modified(x))):
                yield (self.get_file_metadata(x), self.get_file_text(x))


    def execute_queries(
        self,
        queries,
        definitions=None,
        meta_filter=None,
        exclude_modified=False):
        """Runs the given queries on the corpus asynchronously.

        Arguments:
            queries ([Query]): The queries to run.
            definitions (dict): A dictionary defining query terms.
            meta_filter (dict -> bool): A function taking file meta data and
                returning whether the file should be queried.
            exclude_modified (bool): Whether to exclude modified files from
                the query.

        Returns:
            [Result]: An iterator producing the results of the query.
        """
        log = logging.getLogger('uweclang.corpus.manager')
        results = []

        # Get filtered files from corpus.
        try:
            files = self.files(
                meta_filter=meta_filter,
                exclude_modified=exclude_modified)
        except Exception as e:
            raise CorpusException(e)

        try:
            log.debug('Executing query batch.')
            for index, (meta, tagged) in enumerate(files):
                # Extract TaggedToken list from file.
                text = list(chain.from_iterable(uweclang.read_tagged_string(tagged)))
                # Execute search.
                for i, query in enumerate(queries):
                    log.debug('Running query #%d on file #%d', i,  index)
                    res = query.match(text, source_id=index, definitions=definitions)
                    if res:
                        results.append(res)

            return chain.from_iterable(results)
        except Exception as e:
            raise QueryExecutionError(e)

    def execute_queries_async(
        self,
        queries,
        definitions=None,
        meta_filter=None,
        exclude_modified=False):
        """Runs the given queries on the corpus asynchronously.

        Arguments:
            queries ([Query]): The queries to run.
            definitions (dict): A dictionary defining query terms.
            meta_filter (dict -> bool): A function taking file meta data and
                returning whether the file should be queried.
            exclude_modified (bool): Whether to exclude modified files from
                the query.

        Returns:
            [Result]: An iterator producing the results of the query.
        """
        log = logging.getLogger('uweclang.corpus.manager')
        results = []

        # Get filtered files from corpus.
        try:
            files = self.files(
                meta_filter=meta_filter,
                exclude_modified=exclude_modified)
        except Exception as e:
            raise CorpusException(e)

        status = {
            'completed' : 0,
            'total': 0,
        } # Dictionary needed since `nonlocal` is not in Python 2.7.

        log.debug('Executing query batch (async.)')
        # Function for searching a single file.
        def query_file(meta, tagged, index):
            results = []
            # Extract TaggedToken list from file.
            text = list(chain.from_iterable(uweclang.read_tagged_string(tagged)))
            # Execute search.
            try:
                for i, query in enumerate(queries):
                    res = query.match(text, source_id=index, definitions=definitions)
                    if res:
                        results.extend(res)
            except Exception as e:
                raise QueryExecutionError(e)

            # Update status variables.
            status['completed'] += 1
            log.debug('Completed file %d', index)
            percent = int(status['completed'] / status['total'] * 100)
            log.info('%d%% complete', percent)
            return results

        # Worker function for running a file search.
        @asyncio.coroutine
        def worker(meta, tagged, index):
            log.debug('Starting file %d', index)
            return loop.run_in_executor(None, query_file, meta, tagged, index)

        # Create asynchronous task list.
        loop = asyncio.get_event_loop()
        tasks = []
        for index, (meta, tagged) in enumerate(files):
            log.debug('Added task %d', index)
            tasks.append(asyncio.ensure_future(worker(meta, tagged, index)))

        # Run tasks.
        status['total'] = len(tasks)
        log.info('Starting %d tasks.', status['total'])
        data = loop.run_until_complete(asyncio.gather(*tuple(tasks)))

        # Shutdown event loop and logger.
        loop.close()
        logging.shutdown()

        results = (task.result() for task in tasks if task.result())
        return chain.from_iterable(results)
