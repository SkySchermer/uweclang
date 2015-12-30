# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from uweclang import Corpus
from pprint import pprint

if __name__ == '__main__':
    print('Testing full corpus creation.')
    c = Corpus(search_locations=['./test'], extensions=['.tag.txt'])
    files = list(c.get_file_ids())
    assert len(files) == 10

    print('Testing partial corpus creation.')
    c2 = Corpus()
    c2.add_files(['./test/example_a.tag.txt'])
    files = list(c2.get_file_ids())
    assert len(files) == 1
    c2.add_files(['./test/example_b.tag.txt'])
    files = list(c2.get_file_ids())
    assert len(files) == 2

    print('Showing corpus metadata:')
    pprint(c.get_file_metadata(8))


    print('Showing corpus text:')
    pprint(c.get_file_text(5))

    print('Showing corpus ids:')
    for f in c.get_file_ids():
        fdat = c.get_file_metadata(f)
        print(fdat['base'], c.get_id_for_file(fdat['location']))

    mod_file = 3
    print('Modifying a file:', mod_file)
    with open(c.get_file_metadata(mod_file)['location'], 'a') as f:
        f.write(' ')
    print('Detect file modifications:')
    for f in c.get_file_ids():
        if c.file_modified(f):
            print('File', f, 'modified.')

