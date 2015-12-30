"""UWEC Language Tools query module

    Provides functions for defining and executing corpus queries.
"""
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from itertools import chain

from uweclang.query.grammar.QueryLexer import QueryLexer
from uweclang.query.grammar.QueryParser import QueryParser
from uweclang.query.grammar.basic import BasicListener, BasicErrorListener
from antlr4 import *

# Setup logger.
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

class QueryDocument(object):
    """Represents the result of a parsed query document.
    """
    def __init__(self, input_stream):
        lexer = QueryLexer(InputStream(input_stream))
        stream = CommonTokenStream(lexer)
        parser = QueryParser(stream)
        parser._listeners = [BasicErrorListener()]
        tree = parser.queryDocument()

        query_parser = BasicListener()
        walker = ParseTreeWalker()
        walker.walk(query_parser, tree)

        self._errors = query_parser.errors
        self._definitions = query_parser.definitions
        self._queries = query_parser.queries

    @property
    def definitions(self):
        """A dict of the parsed definitions. """
        return self._definitions if not self.errors else None

    @property
    def queries(self):
        """A list of the parsed queries. """
        return self._queries if not self.errors else None

    @property
    def errors(self):
        """A list of parsing errors. """
        return self._errors
