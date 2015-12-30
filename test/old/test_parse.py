# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals


from antlr4 import *
from uweclang import Corpus

import sys
import re
from pprint import pprint


# Debug/Testing:
from uweclang import *

def main(argv):
    inp = FileStream(argv[1])
    # inp = InputStream('define xyz [a, b, c]')
    doc = QueryDocument(inp)

    for e in doc.errors:
        print(e)

    if not doc.errors:
        for k, v in doc.definitions.items():
            print('define', k, v)

        c = Corpus(search_locations=['./test'], extensions=['.tag.txt'])
        for q in doc.queries:
            print(q)
            q.execute(c, definitions=doc.definitions)

if __name__ == '__main__':
    main(sys.argv)
