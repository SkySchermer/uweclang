# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import re
import filecmp
from uweclang import Corpus, QueryDocument, get_files, split_ext
from uweclang import StudentCorpus, select_sem, select_classes, compile_statistics
from pprint import pprint
from time import clock

# Configure logging.
import logging
logger = logging.getLogger('uweclang')
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter(
    '[%(name)s] %(filename)s:%(lineno)d: %(levelname)s %(message)s'
))
logger.addHandler(sh)
logger.setLevel(logging.INFO)

_CORPUS_SELECTOR = re.compile(r'//\s*Corpus:\s*(\S*)', re.I)


def main(argv):
    # Setup root of test folder.
    if len(argv) > 1:
        root = argv[1]
    else:
        root = './test'

    # Create test corpora
    full_corpus = StudentCorpus(
        search_locations=[root + '/corpus'],
        extensions=['.tag.txt'])
    simple_corpus = Corpus(
        search_locations=[root + '/corpus/z.tag.txt'])

    corpora = {
        'full' : full_corpus,
        'simple' : simple_corpus,
    }

    # Get test files
    tests, test_count = get_files([root + '/query'])
    print('Running {} tests: '.format(test_count), end='')
    summary = []

    for test in tests:
        # Get test file name for expected and actual.
        file_name = split_ext(test)[0]
        out_file_name = root + '/actual/' + file_name
        comp_file_name = root + '/expected/' + file_name

        with open(test) as in_file:
            # Select corpus
            corpus = corpora.get(
                _CORPUS_SELECTOR.match(in_file.readline()).group(1),
                full_corpus)

            # Read and Parse query
            doc = QueryDocument(in_file.read())
            if doc.errors:
                pprint(doc.errors)
            else:
                # Clear previous data.
                open(out_file_name, 'w').close()
                run_time = 0
                for query in doc.queries:
                    # Execute query.
                    start_time = clock()
                    result = query.execute(
                        corpus,
                        definitions=doc.definitions)
                    end_time = clock()
                    run_time += end_time-start_time
                    # result = list(result)
                    # pprint(list(result))
                    # pprint(process_statistics(result, corpus, categories=['size', 'location']))

                    # Write results to file.
                    with open(out_file_name, 'a+') as out_file:
                        out_file.write('\n'.join(map(str, result)))
                        out_file.write('\n')

                avg_time = run_time / len(doc.queries)

                # Compare results to expected and add to summary.
                same = filecmp.cmp(out_file_name, comp_file_name)
                summary.append((file_name, same, run_time, avg_time))
                print('.', end='')
                sys.stdout.flush()


    # Print results.
    print()
    print('-'*22, 'Summary', '-'*22)
    passed = 0
    summary.sort(key=(lambda x:x[0]))
    for i, (file_name, same, run_time, avg_time) in enumerate(summary):
        if same:
            passed += 1
        print(' {:<3} [{}] {:<20} RUN {:0.3f}s  AVG {:0.3f}s'.format(
            i,
            'X' if same else ' ',
            file_name,
            run_time,
            avg_time))
    print('-'*22, '{:>3}/{:<3}'.format(passed, len(summary)), '-'*22)



if __name__ == '__main__':
    main(sys.argv)
