# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
from pprint import pprint
from antlr4 import *


from uweclang.query.abstract import *
from uweclang.query.query import *
from uweclang.tagged.tag import TaggedToken
from uweclang.corpus.manager import *

def test_all(name, tests):
    results = []
    passed, total = (0, len(tests))
    for test in tests:
        if test:
            passed += 1
    results.append('[{}] {:<60} {} of {} passed'.format(
        'X' if passed == total else ' ',
        name,
        passed,
        total))
    return results

def main(argv):
    results = []

    results.extend(test_all('Functional._regex_matches()', [
        not Functional._regex_matches(r'abc', TaggedToken('abcd', 'N')),
        Functional._regex_matches(r'abcd', TaggedToken('abcd', 'N')),
        not Functional._regex_matches(r'abcde', TaggedToken('abcd', 'N')),
    ]))

    results.extend(test_all('Functional._clear_cache()', [
        Functional._clear_cache() is None,
        Functional._regex_cache == {},
    ]))

    doc = QueryDocument(InputStream(r"""
        a b:tag:N c d e;
        a b \1 \2;
        a b;
        ~b a;
    """))
    data = list(uweclang.read_tagged_string('a/N b/V a/N b/N c/V d/N e/N'))[0]
    out = [
        list(uweclang.read_tagged_string('a/N b/N c/V d/N e/N')),
        list(uweclang.read_tagged_string('a/N b/V a/N b/N')),
        list(uweclang.read_tagged_string('a/N b/V\na/N b/N')),
        None,
    ]

    results.extend(test_all('Query match', [
        [x.match_text for x in doc.queries[0].match(data)] == out[0],
        [x.match_text for x in doc.queries[1].match(data)] == out[1],
        [x.match_text for x in doc.queries[2].match(data)] == out[2],
        not doc.queries[3].match(data)
    ]))

    # Print results.
    print('-'*79)
    for res in results:
        print(res)
    print('-'*79)

    # print(doc.queries[0].match(data)[0].match_text)
    # print(out[0])
if __name__ == '__main__':
    main(sys.argv)
