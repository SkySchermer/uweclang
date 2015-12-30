# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import re
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from uweclang.query.grammar.QueryListener import QueryListener
from uweclang.query.abstract import *
from uweclang.query.result import QueryParseError

# Setup logger.
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

class BasicErrorListener(ErrorListener):
    def __init__(self):
        super(BasicErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise QueryParseError(msg, text=offendingSymbol.text, line=line, column=column)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


def enter_print(f):
    log = logging.getLogger(__name__)
    f_name = re.sub(r'^(enter|exit)', '', f.__name__)
    def func_wrapper(self, ctx):
        f(self, ctx)
        log.debug('{}{}'.format('    '*(ctx.depth()-1), f_name))
    return func_wrapper

def exit_print(f):
    log = logging.getLogger(__name__)
    def func_wrapper(self, ctx):
        f(self, ctx)
    return func_wrapper

def enter_leaf(f):
    log = logging.getLogger(__name__)
    f_name = re.sub(r'^(enter|exit)', '', f.__name__) + ':'
    def func_wrapper(self, ctx):
        f(self, ctx)
        log.debug('{}{}{}'.format('    '*(ctx.depth()-1), f_name, ctx.getText()))
    return func_wrapper



# This class defines a complete listener for a parse tree produced by QueryParser.
class BasicListener(QueryListener):

    def __init__(self):
        super(self.__class__, self).__init__()
        self._errors = []
        self._definitions = None
        self._queries = None
        self._query_stack = []

    @property
    def queries(self):
        return self._queries

    @property
    def definitions(self):
        return self._definitions

    @property
    def errors(self):
        return self._errors

    # Enter a parse tree produced by QueryParser#query_document.
    @enter_print
    def enterQueryDocument(self, ctx):
        """Prepares to receive queries and definitions. """
        self._definitions = dict()
        self._queries = []

    # Exit a parse tree produced by QueryParser#query_document.
    @exit_print
    def exitQueryDocument(self, ctx):
        pass

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#query.
    @enter_print
    def enterQueryStatement(self, ctx):
        """Prepares to receive a query. """
        self._query = Query()
        self._back_references = []

    # Exit a parse tree produced by QueryParser#query.
    @exit_print
    def exitQueryStatement(self, ctx):
        """Stores the query. """
        self._queries.append(self._query)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#Definition.
    @enter_print
    def enterDefinition(self, ctx):
        """Prepares to receive a definition query. """
        self._identifier = None
        self._query = Query()

    # Exit a parse tree produced by QueryParser#Definition.
    @exit_print
    def exitDefinition(self, ctx):
        """Stores the definition. """
        self._definitions[self._identifier] = self._query

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#query.
    @enter_print
    def enterQuery(self, ctx):
        """Prepares to receive terms. """
        self._terms = []

    # Exit a parse tree produced by QueryParser#query.
    @exit_print
    def exitQuery(self, ctx):
        """Stores parsed terms in query. """
        self._query.terms.extend(self._terms)


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#NegativeTerm.
    @enter_print
    def enterNegativeTerm(self, ctx):
        """Prepares to receive term. """
        self._term = Term()

    # Exit a parse tree produced by QueryParser#NegativeTerm.
    @exit_print
    def exitNegativeTerm(self, ctx):
        """Stores the negated term. """
        self._term.negated = True
        self._terms.append(self._term)


    # Enter a parse tree produced by QueryParser#PositiveTerm.
    @enter_print
    def enterPositiveTerm(self, ctx):
        """Prepares to receive term. """
        self._term = Term()

    # Exit a parse tree produced by QueryParser#PositiveTerm.
    @exit_print
    def exitPositiveTerm(self, ctx):
        """Stores the term. """
        self._term.negated = False
        self._terms.append(self._term)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#SubQueryTerm.
    @enter_print
    def enterSubQueryTerm(self, ctx):
        """Prepares to receive query group with quantifier. Hides the current
        query.
        """
        self._quantifier_lower = 1
        self._quantifier_upper = 1
        # Push recursive stack frame.
        self._query_stack.insert(0, (
            self._query,
            self._term,
            self._terms,
            self._back_references,
        ))
        self._query = Query()
        self._term = Term()
        self._terms = []
        self._back_references = []

    # Exit a parse tree produced by QueryParser#SubQueryTerm.
    @exit_print
    def exitSubQueryTerm(self, ctx):
        """Stores the subquery as a term and restores the previous query. """
        # Pop recursive stack frame.
        (
            original_query,
            self._term,
            self._terms,
            self._back_references,
        ) = self._query_stack.pop(0)

        self._term.quantifier = (self._quantifier_lower, self._quantifier_upper)
        self._term.sub_query = self._query
        self._query = original_query

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#SimpleTerm.
    @enter_print
    def enterSimpleTerm(self, ctx):
        """Prepares to receive match functions. """
        self._match_functions = []

    # Exit a parse tree produced by QueryParser#SimpleTerm.
    @exit_print
    def exitSimpleTerm(self, ctx):
        """Stores parse match functions in the current term. """
        self._term.match_functions = self._match_functions

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#IntersectionTerm.
    @enter_print
    def enterIntersectionTerm(self, ctx):
        """Prepares to receive match functions. """
        self._match_functions = []

    # Exit a parse tree produced by QueryParser#IntersectionTerm.
    @exit_print
    def exitIntersectionTerm(self, ctx):
        """Stores parse match functions in the current term. """
        self._term.match_functions = self._match_functions

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#DirectApply.
    @enter_print
    def enterDirectApply(self, ctx):
        """Prepares to receive functionals. """
        # Prepare implicit match functional.
        implicit_functional = Functional()
        implicit_functional.items.add(Functional._IMPLICIT_MATCH)
        self._functionals = [implicit_functional]

    # Exit a parse tree produced by QueryParser#DirectApply.
    @exit_print
    def exitDirectApply(self, ctx):
        """Stores parsed functionals in match function. """
        match_function = MatchFunction()
        match_function.functionals.extend(self._functionals)
        self._match_functions.append(match_function)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#MatchApply.
    @enter_print
    def enterMatchApply(self, ctx):
        """Prepares to receive functionals. """
        self._functionals = []

    # Exit a parse tree produced by QueryParser#MatchApply.
    @exit_print
    def exitMatchApply(self, ctx):
        """Stores parsed functionals in match function. """
        match_function = MatchFunction()
        match_function.functionals.extend(self._functionals)
        self._match_functions.append(match_function)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#BackReferenceApply.
    @enter_print
    def enterBackReferenceApply(self, ctx):
        """Prepares to receive functionals. """
        self._functionals = []

    # Exit a parse tree produced by QueryParser#BackReferenceApply.
    @exit_print
    def exitBackReferenceApply(self, ctx):
        """Stores parsed functionals in match function. """
        match_function = MatchFunction()
        match_function.back_reference = self._back_reference
        match_function.functionals.extend(self._functionals)
        self._match_functions.append(match_function)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#NegativeFunctional.
    @enter_print
    def enterNegativeFunctional(self, ctx):
        """Prepares to receive a functional. """
        self._functional = Functional()

    # Exit a parse tree produced by QueryParser#NegativeFunctional.
    @exit_print
    def exitNegativeFunctional(self, ctx):
        """Negates the parsed functional. """
        self._functional.negated = True
        self._functionals.append(self._functional)


    # Enter a parse tree produced by QueryParser#PositiveFunctional.
    @enter_print
    def enterPositiveFunctional(self, ctx):
        """Prepares to receive a Functional. """
        self._functional = Functional()

    # Exit a parse tree produced by QueryParser#PositiveFunctional.
    @exit_print
    def exitPositiveFunctional(self, ctx):
        """Ensures the parsed functional is not negated. """
        self._functional.negated = False
        self._functionals.append(self._functional)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#functional.
    @enter_leaf
    def enterImplicitFunctional(self, ctx):
        """Stores the parsed functional. """
        self._functional.items.add(ctx.getText())

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#functional.
    @enter_leaf
    def enterExplicitFunctional(self, ctx):
        """Stores the parsed functional. """
        self._functional.items.add(ctx.getText()[1:-1])

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#ListFunctional.
    @enter_print
    def enterListFunctional(self, ctx):
        """Does nothing. """

    # Exit a parse tree produced by QueryParser#ListFunctional.
    @exit_print
    def exitListFunctional(self, ctx):
        """Does nothing. """

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#backreference.
    @enter_print
    def enterBackReference(self, ctx):
        """Prepares to receive back reference. """
        self._numbers = []

    # Exit a parse tree produced by QueryParser#backreference.
    @exit_print
    def exitBackReference(self, ctx):
        """Stores the backreference. """
        self._back_reference = self._numbers[0]
        self._back_references.append(self._numbers[0])

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#identifier.
    @enter_leaf
    def enterIdentifier(self, ctx):
        """Stores the identifier. """
        self._identifier = ctx.getText()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#QuantifierZeroOrOne.
    @enter_print
    def enterQuantifierZeroOrOne(self, ctx):
        """Does nothing. """

    # Exit a parse tree produced by QueryParser#QuantifierZeroOrOne.
    @exit_print
    def exitQuantifierZeroOrOne(self, ctx):
        """Stores the quantifier bounds. """
        self._quantifier_lower = 0;
        self._quantifier_upper = 1;

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#QuantifierN.
    @enter_print
    def enterQuantifierN(self, ctx):
        """Prepares to receive quantifier amount. """
        self._numbers = []

    # Exit a parse tree produced by QueryParser#QuantifierN.
    @exit_print
    def exitQuantifierN(self, ctx):
        """Stores the quantifier bounds. """
        self._quantifier_lower = self._numbers[0];
        self._quantifier_upper = self._numbers[0];

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#QuantifierNtoM.
    @enter_print
    def enterQuantifierNtoM(self, ctx):
        """Prepares to receive quantifier bounds. """
        self._numbers = []

    # Exit a parse tree produced by QueryParser#QuantifierNtoM.
    @exit_print
    def exitQuantifierNtoM(self, ctx):
        """Stores the quantifier bounds. """
        self._quantifier_lower = self._numbers[0]
        self._quantifier_upper = self._numbers[1]

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#Quantifier0toN.
    @enter_print
    def enterQuantifier0toN(self, ctx):
        """Prepares to receive quantifier bounds. """
        self._numbers = []

    # Exit a parse tree produced by QueryParser#Quantifier0toN.
    @exit_print
    def exitQuantifier0toN(self, ctx):
        """Stores the quantifier bounds. """
        self._quantifier_lower = 0;
        self._quantifier_upper = self._numbers[0]

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Enter a parse tree produced by QueryParser#number.
    @enter_leaf
    def enterNumber(self, ctx):
        """Stores the parsed number in self._number. """
        num = int(ctx.getText())
        self._numbers.append(num)
