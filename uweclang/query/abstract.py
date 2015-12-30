"""UWEC Language Tools abstract module

    Provides functions for defining and executing corpus queries.

    Important classes:

        Functional -- Represents the application of a functional on a
            TaggedToken.
        MatchFunction -- Represents the application of a sequence of
            functionals on a TaggedToken.
        Term -- Represents a single term in a query.
        Query -- Represents a sequence of terms.

    Each of these classes provides a match() function whose purpose is to
    execute that leg of a query on a list of TaggedTokens. We go into detail
    here about what each match function requires and returns:

    Functional.match():
        Handles function application, definition lookup, and regex matching.
        Can be negated.

        Requires a list of tokens. Function application and regex matching
        typically only need a single token, but if a list is provided, any
        transformations or matches in the list will be returned. A definition
        lookup will forward the entire token list to the query provided by the
        definition.

        Returns those tokens that match the functional.

    MatchFunction.match():
        Applies a sequence of functionals within a term. Each functional is
        applied to the output of the previous.

        Requires a list of tokens and any previous terms matched. Previous
        terms are used to do backreferences. Functionals are applies to the
        tokens.

    Term.match():
        Applies a match function to a single term. A term may be a subquery,
        and that subquery may be quantified. Can be negated.

    Query.match():
        Applies a sequence of terms to a given list of tokens.


"""
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

from itertools import chain
import functools

# Standard imports
import re
import sys

from uweclang.query.result import *
import uweclang

# Setup logger.
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

class Functional(object):
    """Represents a part of a compiled query.
    """
    # Static match function library.
    _match_functions = {
        'tag' : uweclang.TaggedToken.tag_promoted,
    }

    # Regex cache for performance boosts.
    _regex_cache = {}

    # Regex for matching any word for DirectApply rule.
    _IMPLICIT_MATCH = r'.*'

    @staticmethod
    def _clear_cache():
        """Clears the regex cache. """
        Functional._regex_cache = {}

    def __init__(self):
        self._items = set()
        self._negated = False

    @property
    def negated(self):
        return self._negated

    @negated.setter
    def negated(self, value):
        self._negated = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    def __str__(self):
        items = list(self._items)
        res = ''
        if self._negated:
            res += '~'
        if len(items) == 1:
            res += items[0]
        else:
            res += '['
            res += ', '.join(items)
            res += ']'
        return res

    @staticmethod
    def _regex_matches(regex_str, tagged_token):
        regex = Functional._regex_cache.get(regex_str,
                                            re.compile('^' + regex_str + '$',
                                                       flags=re.IGNORECASE))
        Functional._regex_cache[regex_str] = regex

        if regex.match(tagged_token.token):
            return True
        return False

    def match(self, tokens, enable_functions=True, definitions=None, **kwargs):
        """Matches the Functional against the start of the given tokens.

        Arguments:

        Returns:
            [TaggedTokens]: A list of tokens matched by the functional.

        Typically, this will return a single token for a normal match, or None
        if the first token doesn't match. It will return more tokens if
        """
        # FUNCTIONAL
        # DEFINED_QUERY
        # :function
        # literal
        # [a, b, c]
        if not tokens:
            return None

        v = tokens[0]
        f_results = []

        for item in self.items:
            # Apply function
            if (enable_functions and item in Functional._match_functions):
                v = Functional._match_functions[item](v)
                f_results.append(v)

            # Apply definition
            elif definitions and item in definitions:
                def_query = definitions[item]
                if def_query:
                    # Definitions are disabled inside other definitions.
                    f_results = def_query.match(
                        tokens,
                        definitions=None,
                        left_match=True,
                        **kwargs)
                    # Undo query result.
                    if f_results:
                        if self.negated:
                            return None
                        # TODO Decide whether to process multiple results.
                        f_results = f_results[0].match_text

            # Apply regex
            else:
                if item == '.*' or Functional._regex_matches(item, v):
                    if self.negated: return None
                    f_results.append(v)
                elif self.negated:
                    return [v]

        return f_results if f_results and not self.negated else None




class MatchFunction(object):

    def __init__(self):
        self._functionals = []
        self._back_reference = None

    @property
    def functionals(self):
        return self._functionals

    @functionals.setter
    def functionals(self, functionals):
        self._functionals = functionals

    @property
    def back_reference(self):
        return self._back_reference

    @back_reference.setter
    def back_reference(self, back_reference):
        self._back_reference = back_reference

    def __str__(self):
        res = ''
        if self._back_reference is not None:
            res += '\\' + str(self._back_reference)
            if self._functionals:
                res += ':'
        res += ':'.join(str(f) for f in self._functionals)
        return res


    def match(self, tokens, previous_terms=None, **kwargs):
        """Applies the match function against the start of the given tokens. """
        # MATCH_FUNCTION
        # a
        # :a
        # a:b
        # "a":b:c
        # \0
        if not tokens:
            return None
        match = tokens
        if not self.back_reference:
            # Handle first functional.
            match = self.functionals[0].match(
                match,
                enable_functions=False,
                **kwargs)
        elif previous_terms:
            # Handle backreference.
            prev = previous_terms[self.back_reference-1]
            for i in range(0, len(prev)):
                if kwargs.get('backreferences_match_tags', False):
                    if tokens[i] != prev[i]:
                        return None
                else:
                    if tokens[i].token != prev[i].token:
                        return None
            return tokens[:len(prev)]
        else:
            return None

        # Handle match function tail.
        for functional in self.functionals[1:]:
            # print('    Functional applying "{}" to {}'.format(functional, match))
            if not match: break
            match = functional.match(match, enable_functions=True, **kwargs)
            # print('    >', match)
        return tokens[0:len(match)] if match else None



class Term(object):
    """Represents a term of a compiled query.
    """
    def __init__(self):
        self._match_functions = []
        self._negated = False
        self._sub_query = None
        self._quantifier = (1, 1)

    @property
    def negated(self):
        return self._negated

    @negated.setter
    def negated(self, value):
        self._negated = value

    @property
    def sub_query(self):
        return self._sub_query

    @sub_query.setter
    def sub_query(self, query):
        self._sub_query = query

    @property
    def quantifier(self):
        return self.quantifier

    @quantifier.setter
    def quantifier(self, quantifier):
        self._quantifier = quantifier

    @property
    def match_functions(self):
        return self._match_functions

    @match_functions.setter
    def match_functions(self, match_functions):
        self._match_functions = match_functions

    def __str__(self):
        res = ''
        if self._negated:
            res += '~'
        if self._sub_query:
            # Add sub query.
            res += '({})'.format(self._sub_query)
            if self._quantifier == (0,1):
                # Add ? quantifier.
                res += '?'
            elif (self._quantifier != (1,1)
                  and self._quantifier[0] == self._quantifier[1]):
                # Add {n} quantifier.
                res += '{{{}}}'.format(self._quantifier[0])
            elif self._quantifier != (1,1):
                # Add {,m} and {n,m} quantifiers.
                res += '{{{},{}}}'.format(
                    self._quantifier[0] if self._quantifier[0] != 0 else '',
                    self._quantifier[1]
                )
        else:
            # Add intersecting terms.
            res += '::'.join(str(f) for f in self._match_functions)
        return res

    def match(self, tokens, **kwargs):
        """Applies match functions to the start of the given tokens. """
        # TERM
        # a
        # a::b
        # ~a
        # (a){n,m}
        if not tokens:
            return None

        # print('  Term Match "{}" on "{}..."'.format(self, uweclang.tagged_to_plain([tokens[0:2]])))

        result = []
        for match_function in self.match_functions:
            result = match_function.match(tokens, **kwargs)
            if not result:
                break
            # print('  Match Function: "{}" = {}'.format(match_function, result))

        if not result and self.negated:
            return [tokens[0]]
        return result if result and not self.negated else None



class Query(object):
    """Represents a parsed, executable query.
    """
    def __init__(self):
        self._terms = []

    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, terms):
        self._terms = terms

    def __str__(self):
        res = ' '.join(str(t) for t in self._terms)
        return res

    def match(
        self,
        tokens,
        source_id=None,
        overlapping=True,
        left_match=False,
        **kwargs):
        """
        """
        if not tokens:
            return None
        # QUERY
        # Occurences will contain each resulting match in the query.
        occurences = []
        # print('Query("{}")'.format(self))
        i = 0
        while i < len(tokens):
            # print()
            term_results = []
            term_offset = 0
            for term in self.terms:
                # Match the term against the tokens not yet matched.
                term_result = term.match(
                    tokens[i+term_offset:],
                    previous_terms=term_results,
                    **kwargs);

                # Move to next token if term fails to match.
                if not term_result:
                    term_results = []
                    break

                # Otherwise, move to the next term and store the matched
                # values.
                term_offset += len(term_result)
                term_results.append(term_result)

            # Append (flattened) match to the list of occurences.
            if term_results:
                match_text = list(chain.from_iterable(term_results))
                result = QueryResult(
                    match_text,
                    span=(i, i + len(match_text) - 1),
                    source_id=source_id)
                occurences.append(result)
                # print("* Query match: '{}' @{} ".format(result, result.span))

            if left_match:
                break

            # Advence to next token position.
            if term_results and not overlapping:
                i += len(term_results)
            else:
                i += 1

        return occurences

    def execute(
        self,
        corpus,
        definitions=None,
        meta_filter=None,
        exclude_modified=False,
        overlapping=True):
        """Executes the query on the given corpus.
        """
        logger = logging.getLogger('uweclang')

        results = []
        # Get filtered files from corpus.
        try:
            files = corpus.files(
                meta_filter=meta_filter,
                exclude_modified=exclude_modified)
        except Exception as e:
            raise CorpusException(e)

        try:
            logger.debug('Starting query')
            for index, (meta, tagged) in enumerate(files):
                # Extract TaggedToken list from file.
                text = list(chain.from_iterable(uweclang.read_tagged_string(tagged)))
                # Execute search.
                res = self.match(text, source_id=index, definitions=definitions)
                if res:
                    results.append(res)

            return chain.from_iterable(results)
        except Exception as e:
            raise QueryExecutionError(e)

