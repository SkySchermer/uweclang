# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by QueryParser.

class QueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QueryParser#queryDocument.
    def visitQueryDocument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#QueryStatement.
    def visitQueryStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#Definition.
    def visitDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#query.
    def visitQuery(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#NegativeTerm.
    def visitNegativeTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#PositiveTerm.
    def visitPositiveTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#SubQueryTerm.
    def visitSubQueryTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#SimpleTerm.
    def visitSimpleTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#IntersectionTerm.
    def visitIntersectionTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#DirectApply.
    def visitDirectApply(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#MatchApply.
    def visitMatchApply(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#BackReferenceApply.
    def visitBackReferenceApply(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#NegativeFunctional.
    def visitNegativeFunctional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#PositiveFunctional.
    def visitPositiveFunctional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ExplicitFunctional.
    def visitExplicitFunctional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ImplicitFunctional.
    def visitImplicitFunctional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ListFunctional.
    def visitListFunctional(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#backReference.
    def visitBackReference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#QuantifierZeroOrOne.
    def visitQuantifierZeroOrOne(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#QuantifierN.
    def visitQuantifierN(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#QuantifierNtoM.
    def visitQuantifierNtoM(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#Quantifier0toN.
    def visitQuantifier0toN(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueryParser#ws.
    def visitWs(self, ctx):
        return self.visitChildren(ctx)


