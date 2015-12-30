"""UWEC Language Tools corpus.student module

    Provides functions for defining and managing a student corpus.
"""
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import re
from uweclang.corpus.manager import default_metadata_function, Corpus

# Setup logger.
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


def student_metadata_function(filename):
    """
    """
    # Collect basic metadata:
    metadata = default_metadata_function(filename)

    if not metadata: return None
    # Collect student metadata:

    base_name = metadata['base']
    match = re.match(r'(\d+)-([fs]\d\d)-(\d+)', base_name, re.IGNORECASE)
    if match:
        metadata['class'] = match.group(1)
        metadata['semester'] = match.group(2)
        metadata['paper_id'] = match.group(3)

    return metadata


class StudentCorpus(Corpus):
    """A corpus object for managing a collection of tagged text files.
    """
    def __init__(self,
                 search_locations=[],
                 extensions=['.tag.txt'],
                 recursive=False):
        super(StudentCorpus, self).__init__(
            search_locations=search_locations,
            extensions=extensions,
            recursive=recursive,
            meta_op=student_metadata_function)


def select_classes(classes):
    return lambda x: x.get('class') in classes

def select_sem(semesters):
    return lambda x: x.get('semester') in semesters
