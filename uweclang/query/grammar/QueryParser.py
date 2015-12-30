# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .QueryListener import QueryListener
    from .QueryVisitor import QueryVisitor
else:
    from QueryListener import QueryListener
    from QueryVisitor import QueryVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\27\u00da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\3\2\5\2\36\n\2\3\2\3\2\5\2\"\n\2\3\2\3\2")
        buf.write(u"\5\2&\n\2\7\2(\n\2\f\2\16\2+\13\2\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\5\3\64\n\3\5\3\66\n\3\3\4\3\4\3\4\3\4\7\4<\n")
        buf.write(u"\4\f\4\16\4?\13\4\3\5\3\5\3\5\5\5D\n\5\3\6\3\6\3\6\3")
        buf.write(u"\6\5\6J\n\6\3\6\3\6\3\6\3\6\6\6P\n\6\r\6\16\6Q\5\6T\n")
        buf.write(u"\6\3\7\3\7\6\7X\n\7\r\7\16\7Y\3\7\3\7\3\7\7\7_\n\7\f")
        buf.write(u"\7\16\7b\13\7\3\7\3\7\3\7\7\7g\n\7\f\7\16\7j\13\7\5\7")
        buf.write(u"l\n\7\3\b\3\b\3\b\5\bq\n\b\3\t\3\t\3\t\3\t\3\t\5\tx\n")
        buf.write(u"\t\3\t\3\t\5\t|\n\t\3\t\3\t\5\t\u0080\n\t\3\t\7\t\u0083")
        buf.write(u"\n\t\f\t\16\t\u0086\13\t\3\t\5\t\u0089\n\t\3\t\5\t\u008c")
        buf.write(u"\n\t\3\t\5\t\u008f\n\t\3\t\3\t\5\t\u0093\n\t\3\n\3\n")
        buf.write(u"\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u009d\n\f\3\f\3\f\5\f")
        buf.write(u"\u00a1\n\f\3\f\3\f\3\f\3\f\5\f\u00a7\n\f\3\f\3\f\5\f")
        buf.write(u"\u00ab\n\f\3\f\3\f\5\f\u00af\n\f\3\f\3\f\5\f\u00b3\n")
        buf.write(u"\f\3\f\3\f\3\f\3\f\5\f\u00b9\n\f\3\f\3\f\5\f\u00bd\n")
        buf.write(u"\f\3\f\3\f\5\f\u00c1\n\f\3\f\3\f\5\f\u00c5\n\f\3\r\3")
        buf.write(u"\r\3\16\6\16\u00ca\n\16\r\16\16\16\u00cb\3\16\6\16\u00cf")
        buf.write(u"\n\16\r\16\16\16\u00d0\3\16\6\16\u00d4\n\16\r\16\16\16")
        buf.write(u"\u00d5\5\16\u00d8\n\16\3\16\2\2\17\2\4\6\b\n\f\16\20")
        buf.write(u"\22\24\26\30\32\2\3\3\3\3\3\u00f9\2)\3\2\2\2\4\65\3\2")
        buf.write(u"\2\2\6\67\3\2\2\2\bC\3\2\2\2\nS\3\2\2\2\fk\3\2\2\2\16")
        buf.write(u"p\3\2\2\2\20\u0092\3\2\2\2\22\u0094\3\2\2\2\24\u0096")
        buf.write(u"\3\2\2\2\26\u00c4\3\2\2\2\30\u00c6\3\2\2\2\32\u00d7\3")
        buf.write(u"\2\2\2\34\36\5\32\16\2\35\34\3\2\2\2\35\36\3\2\2\2\36")
        buf.write(u"\37\3\2\2\2\37!\5\4\3\2 \"\5\32\16\2! \3\2\2\2!\"\3\2")
        buf.write(u"\2\2\"#\3\2\2\2#%\t\2\2\2$&\5\32\16\2%$\3\2\2\2%&\3\2")
        buf.write(u"\2\2&(\3\2\2\2\'\35\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3")
        buf.write(u"\2\2\2*\3\3\2\2\2+)\3\2\2\2,\66\5\6\4\2-.\7\4\2\2./\5")
        buf.write(u"\32\16\2/\60\5\22\n\2\60\61\5\32\16\2\61\63\5\6\4\2\62")
        buf.write(u"\64\5\32\16\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2")
        buf.write(u"\2\65,\3\2\2\2\65-\3\2\2\2\66\5\3\2\2\2\67=\5\b\5\28")
        buf.write(u"9\5\32\16\29:\5\b\5\2:<\3\2\2\2;8\3\2\2\2<?\3\2\2\2=")
        buf.write(u";\3\2\2\2=>\3\2\2\2>\7\3\2\2\2?=\3\2\2\2@A\7\5\2\2AD")
        buf.write(u"\5\n\6\2BD\5\n\6\2C@\3\2\2\2CB\3\2\2\2D\t\3\2\2\2EF\7")
        buf.write(u"\6\2\2FG\5\6\4\2GI\7\7\2\2HJ\5\26\f\2IH\3\2\2\2IJ\3\2")
        buf.write(u"\2\2JT\3\2\2\2KT\5\f\7\2LO\5\f\7\2MN\7\b\2\2NP\5\f\7")
        buf.write(u"\2OM\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2\2")
        buf.write(u"SE\3\2\2\2SK\3\2\2\2SL\3\2\2\2T\13\3\2\2\2UV\7\t\2\2")
        buf.write(u"VX\5\16\b\2WU\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z")
        buf.write(u"l\3\2\2\2[`\5\16\b\2\\]\7\t\2\2]_\5\16\b\2^\\\3\2\2\2")
        buf.write(u"_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2al\3\2\2\2b`\3\2\2\2ch")
        buf.write(u"\5\24\13\2de\7\t\2\2eg\5\16\b\2fd\3\2\2\2gj\3\2\2\2h")
        buf.write(u"f\3\2\2\2hi\3\2\2\2il\3\2\2\2jh\3\2\2\2kW\3\2\2\2k[\3")
        buf.write(u"\2\2\2kc\3\2\2\2l\r\3\2\2\2mn\7\5\2\2nq\5\20\t\2oq\5")
        buf.write(u"\20\t\2pm\3\2\2\2po\3\2\2\2q\17\3\2\2\2r\u0093\7\21\2")
        buf.write(u"\2s\u0093\7\23\2\2t\u0093\7\22\2\2uw\7\n\2\2vx\5\32\16")
        buf.write(u"\2wv\3\2\2\2wx\3\2\2\2xy\3\2\2\2y{\5\20\t\2z|\5\32\16")
        buf.write(u"\2{z\3\2\2\2{|\3\2\2\2|\u0084\3\2\2\2}\177\7\13\2\2~")
        buf.write(u"\u0080\5\32\16\2\177~\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write(u"\u0081\3\2\2\2\u0081\u0083\5\20\t\2\u0082}\3\2\2\2\u0083")
        buf.write(u"\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2")
        buf.write(u"\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0089")
        buf.write(u"\5\32\16\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write(u"\u008b\3\2\2\2\u008a\u008c\7\13\2\2\u008b\u008a\3\2\2")
        buf.write(u"\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008f")
        buf.write(u"\5\32\16\2\u008e\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write(u"\u0090\3\2\2\2\u0090\u0091\7\f\2\2\u0091\u0093\3\2\2")
        buf.write(u"\2\u0092r\3\2\2\2\u0092s\3\2\2\2\u0092t\3\2\2\2\u0092")
        buf.write(u"u\3\2\2\2\u0093\21\3\2\2\2\u0094\u0095\7\23\2\2\u0095")
        buf.write(u"\23\3\2\2\2\u0096\u0097\7\r\2\2\u0097\u0098\5\30\r\2")
        buf.write(u"\u0098\25\3\2\2\2\u0099\u00c5\7\16\2\2\u009a\u009c\7")
        buf.write(u"\17\2\2\u009b\u009d\5\32\16\2\u009c\u009b\3\2\2\2\u009c")
        buf.write(u"\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\5\30\r")
        buf.write(u"\2\u009f\u00a1\5\32\16\2\u00a0\u009f\3\2\2\2\u00a0\u00a1")
        buf.write(u"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\7\20\2\2\u00a3")
        buf.write(u"\u00c5\3\2\2\2\u00a4\u00a6\7\17\2\2\u00a5\u00a7\5\32")
        buf.write(u"\16\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8")
        buf.write(u"\3\2\2\2\u00a8\u00aa\5\30\r\2\u00a9\u00ab\5\32\16\2\u00aa")
        buf.write(u"\u00a9\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2")
        buf.write(u"\2\u00ac\u00ae\7\13\2\2\u00ad\u00af\5\32\16\2\u00ae\u00ad")
        buf.write(u"\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write(u"\u00b2\5\30\r\2\u00b1\u00b3\5\32\16\2\u00b2\u00b1\3\2")
        buf.write(u"\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5")
        buf.write(u"\7\20\2\2\u00b5\u00c5\3\2\2\2\u00b6\u00b8\7\17\2\2\u00b7")
        buf.write(u"\u00b9\5\32\16\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2")
        buf.write(u"\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc\7\13\2\2\u00bb\u00bd")
        buf.write(u"\5\32\16\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write(u"\u00be\3\2\2\2\u00be\u00c0\5\30\r\2\u00bf\u00c1\5\32")
        buf.write(u"\16\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2")
        buf.write(u"\3\2\2\2\u00c2\u00c3\7\20\2\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write(u"\u0099\3\2\2\2\u00c4\u009a\3\2\2\2\u00c4\u00a4\3\2\2")
        buf.write(u"\2\u00c4\u00b6\3\2\2\2\u00c5\27\3\2\2\2\u00c6\u00c7\7")
        buf.write(u"\22\2\2\u00c7\31\3\2\2\2\u00c8\u00ca\7\24\2\2\u00c9\u00c8")
        buf.write(u"\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write(u"\u00cc\3\2\2\2\u00cc\u00d8\3\2\2\2\u00cd\u00cf\7\26\2")
        buf.write(u"\2\u00ce\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00ce")
        buf.write(u"\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d8\3\2\2\2\u00d2")
        buf.write(u"\u00d4\7\27\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2")
        buf.write(u"\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8")
        buf.write(u"\3\2\2\2\u00d7\u00c9\3\2\2\2\u00d7\u00ce\3\2\2\2\u00d7")
        buf.write(u"\u00d3\3\2\2\2\u00d8\33\3\2\2\2(\35!%)\63\65=CIQSY`h")
        buf.write(u"kpw{\177\u0084\u0088\u008b\u008e\u0092\u009c\u00a0\u00a6")
        buf.write(u"\u00aa\u00ae\u00b2\u00b8\u00bc\u00c0\u00c4\u00cb\u00d0")
        buf.write(u"\u00d5\u00d7")
        return buf.getvalue()


class QueryParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"';'", u"'define'", u"'~'", u"'('", 
                     u"')'", u"'::'", u"':'", u"'['", u"','", u"']'", u"'\\'", 
                     u"'?'", u"'{'", u"'}'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"ExplicitRegex", 
                      u"Digits", u"Symbol", u"WhiteSpace", u"NewLine", u"BlockComment", 
                      u"LineComment" ]

    RULE_queryDocument = 0
    RULE_documentItem = 1
    RULE_query = 2
    RULE_termNegatable = 3
    RULE_term = 4
    RULE_matchFunction = 5
    RULE_functionalNegatable = 6
    RULE_functional = 7
    RULE_identifier = 8
    RULE_backReference = 9
    RULE_quantifier = 10
    RULE_number = 11
    RULE_ws = 12

    ruleNames =  [ u"queryDocument", u"documentItem", u"query", u"termNegatable", 
                   u"term", u"matchFunction", u"functionalNegatable", u"functional", 
                   u"identifier", u"backReference", u"quantifier", u"number", 
                   u"ws" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ExplicitRegex=15
    Digits=16
    Symbol=17
    WhiteSpace=18
    NewLine=19
    BlockComment=20
    LineComment=21

    def __init__(self, input):
        super(QueryParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class QueryDocumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.QueryDocumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def documentItem(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.DocumentItemContext)
            else:
                return self.getTypedRuleContext(QueryParser.DocumentItemContext,i)


        def EOF(self, i=None):
            if i is None:
                return self.getTokens(QueryParser.EOF)
            else:
                return self.getToken(QueryParser.EOF, i)

        def ws(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.WsContext)
            else:
                return self.getTypedRuleContext(QueryParser.WsContext,i)


        def getRuleIndex(self):
            return QueryParser.RULE_queryDocument

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterQueryDocument(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitQueryDocument(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitQueryDocument(self)
            else:
                return visitor.visitChildren(self)




    def queryDocument(self):

        localctx = QueryParser.QueryDocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_queryDocument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.T__1) | (1 << QueryParser.T__2) | (1 << QueryParser.T__3) | (1 << QueryParser.T__6) | (1 << QueryParser.T__7) | (1 << QueryParser.T__10) | (1 << QueryParser.ExplicitRegex) | (1 << QueryParser.Digits) | (1 << QueryParser.Symbol) | (1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                self.state = 27
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 26
                    self.ws()


                self.state = 29
                self.documentItem()
                self.state = 31
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 30
                    self.ws()


                self.state = 33
                _la = self._input.LA(1)
                if not(_la==QueryParser.EOF or _la==QueryParser.T__0):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 35
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 34
                    self.ws()


                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DocumentItemContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.DocumentItemContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_documentItem

     
        def copyFrom(self, ctx):
            super(QueryParser.DocumentItemContext, self).copyFrom(ctx)



    class DefinitionContext(DocumentItemContext):

        def __init__(self, parser, ctx): # actually a QueryParser.DocumentItemContext)
            super(QueryParser.DefinitionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ws(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.WsContext)
            else:
                return self.getTypedRuleContext(QueryParser.WsContext,i)

        def identifier(self):
            return self.getTypedRuleContext(QueryParser.IdentifierContext,0)

        def query(self):
            return self.getTypedRuleContext(QueryParser.QueryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterDefinition(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitDefinition(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)


    class QueryStatementContext(DocumentItemContext):

        def __init__(self, parser, ctx): # actually a QueryParser.DocumentItemContext)
            super(QueryParser.QueryStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def query(self):
            return self.getTypedRuleContext(QueryParser.QueryContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterQueryStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitQueryStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitQueryStatement(self)
            else:
                return visitor.visitChildren(self)



    def documentItem(self):

        localctx = QueryParser.DocumentItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_documentItem)
        try:
            self.state = 51
            token = self._input.LA(1)
            if token in [QueryParser.T__2, QueryParser.T__3, QueryParser.T__6, QueryParser.T__7, QueryParser.T__10, QueryParser.ExplicitRegex, QueryParser.Digits, QueryParser.Symbol]:
                localctx = QueryParser.QueryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.query()

            elif token in [QueryParser.T__1]:
                localctx = QueryParser.DefinitionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(QueryParser.T__1)
                self.state = 44
                self.ws()
                self.state = 45
                self.identifier()
                self.state = 46
                self.ws()
                self.state = 47
                self.query()
                self.state = 49
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.ws()



            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.QueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def termNegatable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.TermNegatableContext)
            else:
                return self.getTypedRuleContext(QueryParser.TermNegatableContext,i)


        def ws(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.WsContext)
            else:
                return self.getTypedRuleContext(QueryParser.WsContext,i)


        def getRuleIndex(self):
            return QueryParser.RULE_query

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterQuery(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitQuery(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = QueryParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.termNegatable()
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 54
                    self.ws()
                    self.state = 55
                    self.termNegatable() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermNegatableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.TermNegatableContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_termNegatable

     
        def copyFrom(self, ctx):
            super(QueryParser.TermNegatableContext, self).copyFrom(ctx)



    class PositiveTermContext(TermNegatableContext):

        def __init__(self, parser, ctx): # actually a QueryParser.TermNegatableContext)
            super(QueryParser.PositiveTermContext, self).__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QueryParser.TermContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterPositiveTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitPositiveTerm(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitPositiveTerm(self)
            else:
                return visitor.visitChildren(self)


    class NegativeTermContext(TermNegatableContext):

        def __init__(self, parser, ctx): # actually a QueryParser.TermNegatableContext)
            super(QueryParser.NegativeTermContext, self).__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(QueryParser.TermContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterNegativeTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitNegativeTerm(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitNegativeTerm(self)
            else:
                return visitor.visitChildren(self)



    def termNegatable(self):

        localctx = QueryParser.TermNegatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_termNegatable)
        try:
            self.state = 65
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = QueryParser.NegativeTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(QueryParser.T__2)
                self.state = 63
                self.term()
                pass

            elif la_ == 2:
                localctx = QueryParser.PositiveTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.TermContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_term

     
        def copyFrom(self, ctx):
            super(QueryParser.TermContext, self).copyFrom(ctx)



    class SimpleTermContext(TermContext):

        def __init__(self, parser, ctx): # actually a QueryParser.TermContext)
            super(QueryParser.SimpleTermContext, self).__init__(parser)
            self.copyFrom(ctx)

        def matchFunction(self):
            return self.getTypedRuleContext(QueryParser.MatchFunctionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterSimpleTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitSimpleTerm(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitSimpleTerm(self)
            else:
                return visitor.visitChildren(self)


    class IntersectionTermContext(TermContext):

        def __init__(self, parser, ctx): # actually a QueryParser.TermContext)
            super(QueryParser.IntersectionTermContext, self).__init__(parser)
            self.copyFrom(ctx)

        def matchFunction(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.MatchFunctionContext)
            else:
                return self.getTypedRuleContext(QueryParser.MatchFunctionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterIntersectionTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitIntersectionTerm(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitIntersectionTerm(self)
            else:
                return visitor.visitChildren(self)


    class SubQueryTermContext(TermContext):

        def __init__(self, parser, ctx): # actually a QueryParser.TermContext)
            super(QueryParser.SubQueryTermContext, self).__init__(parser)
            self.copyFrom(ctx)

        def query(self):
            return self.getTypedRuleContext(QueryParser.QueryContext,0)

        def quantifier(self):
            return self.getTypedRuleContext(QueryParser.QuantifierContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterSubQueryTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitSubQueryTerm(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitSubQueryTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = QueryParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 81
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = QueryParser.SubQueryTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(QueryParser.T__3)
                self.state = 68
                self.query()
                self.state = 69
                self.match(QueryParser.T__4)
                self.state = 71
                _la = self._input.LA(1)
                if _la==QueryParser.T__11 or _la==QueryParser.T__12:
                    self.state = 70
                    self.quantifier()


                pass

            elif la_ == 2:
                localctx = QueryParser.SimpleTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.matchFunction()
                pass

            elif la_ == 3:
                localctx = QueryParser.IntersectionTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.matchFunction()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 75
                    self.match(QueryParser.T__5)
                    self.state = 76
                    self.matchFunction()
                    self.state = 79 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QueryParser.T__5):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MatchFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.MatchFunctionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_matchFunction

     
        def copyFrom(self, ctx):
            super(QueryParser.MatchFunctionContext, self).copyFrom(ctx)



    class DirectApplyContext(MatchFunctionContext):

        def __init__(self, parser, ctx): # actually a QueryParser.MatchFunctionContext)
            super(QueryParser.DirectApplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionalNegatable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.FunctionalNegatableContext)
            else:
                return self.getTypedRuleContext(QueryParser.FunctionalNegatableContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterDirectApply(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitDirectApply(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitDirectApply(self)
            else:
                return visitor.visitChildren(self)


    class BackReferenceApplyContext(MatchFunctionContext):

        def __init__(self, parser, ctx): # actually a QueryParser.MatchFunctionContext)
            super(QueryParser.BackReferenceApplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def backReference(self):
            return self.getTypedRuleContext(QueryParser.BackReferenceContext,0)

        def functionalNegatable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.FunctionalNegatableContext)
            else:
                return self.getTypedRuleContext(QueryParser.FunctionalNegatableContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterBackReferenceApply(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitBackReferenceApply(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitBackReferenceApply(self)
            else:
                return visitor.visitChildren(self)


    class MatchApplyContext(MatchFunctionContext):

        def __init__(self, parser, ctx): # actually a QueryParser.MatchFunctionContext)
            super(QueryParser.MatchApplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functionalNegatable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.FunctionalNegatableContext)
            else:
                return self.getTypedRuleContext(QueryParser.FunctionalNegatableContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterMatchApply(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitMatchApply(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitMatchApply(self)
            else:
                return visitor.visitChildren(self)



    def matchFunction(self):

        localctx = QueryParser.MatchFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_matchFunction)
        self._la = 0 # Token type
        try:
            self.state = 105
            token = self._input.LA(1)
            if token in [QueryParser.T__6]:
                localctx = QueryParser.DirectApplyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 83
                    self.match(QueryParser.T__6)
                    self.state = 84
                    self.functionalNegatable()
                    self.state = 87 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QueryParser.T__6):
                        break


            elif token in [QueryParser.T__2, QueryParser.T__7, QueryParser.ExplicitRegex, QueryParser.Digits, QueryParser.Symbol]:
                localctx = QueryParser.MatchApplyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.functionalNegatable()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==QueryParser.T__6:
                    self.state = 90
                    self.match(QueryParser.T__6)
                    self.state = 91
                    self.functionalNegatable()
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


            elif token in [QueryParser.T__10]:
                localctx = QueryParser.BackReferenceApplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.backReference()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==QueryParser.T__6:
                    self.state = 98
                    self.match(QueryParser.T__6)
                    self.state = 99
                    self.functionalNegatable()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionalNegatableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.FunctionalNegatableContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_functionalNegatable

     
        def copyFrom(self, ctx):
            super(QueryParser.FunctionalNegatableContext, self).copyFrom(ctx)



    class NegativeFunctionalContext(FunctionalNegatableContext):

        def __init__(self, parser, ctx): # actually a QueryParser.FunctionalNegatableContext)
            super(QueryParser.NegativeFunctionalContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functional(self):
            return self.getTypedRuleContext(QueryParser.FunctionalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterNegativeFunctional(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitNegativeFunctional(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitNegativeFunctional(self)
            else:
                return visitor.visitChildren(self)


    class PositiveFunctionalContext(FunctionalNegatableContext):

        def __init__(self, parser, ctx): # actually a QueryParser.FunctionalNegatableContext)
            super(QueryParser.PositiveFunctionalContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functional(self):
            return self.getTypedRuleContext(QueryParser.FunctionalContext,0)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterPositiveFunctional(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitPositiveFunctional(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitPositiveFunctional(self)
            else:
                return visitor.visitChildren(self)



    def functionalNegatable(self):

        localctx = QueryParser.FunctionalNegatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionalNegatable)
        try:
            self.state = 110
            token = self._input.LA(1)
            if token in [QueryParser.T__2]:
                localctx = QueryParser.NegativeFunctionalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(QueryParser.T__2)
                self.state = 108
                self.functional()

            elif token in [QueryParser.T__7, QueryParser.ExplicitRegex, QueryParser.Digits, QueryParser.Symbol]:
                localctx = QueryParser.PositiveFunctionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.functional()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.FunctionalContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_functional

     
        def copyFrom(self, ctx):
            super(QueryParser.FunctionalContext, self).copyFrom(ctx)



    class ListFunctionalContext(FunctionalContext):

        def __init__(self, parser, ctx): # actually a QueryParser.FunctionalContext)
            super(QueryParser.ListFunctionalContext, self).__init__(parser)
            self.copyFrom(ctx)

        def functional(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.FunctionalContext)
            else:
                return self.getTypedRuleContext(QueryParser.FunctionalContext,i)

        def ws(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.WsContext)
            else:
                return self.getTypedRuleContext(QueryParser.WsContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterListFunctional(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitListFunctional(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitListFunctional(self)
            else:
                return visitor.visitChildren(self)


    class ImplicitFunctionalContext(FunctionalContext):

        def __init__(self, parser, ctx): # actually a QueryParser.FunctionalContext)
            super(QueryParser.ImplicitFunctionalContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Symbol(self):
            return self.getToken(QueryParser.Symbol, 0)
        def Digits(self):
            return self.getToken(QueryParser.Digits, 0)

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterImplicitFunctional(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitImplicitFunctional(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitImplicitFunctional(self)
            else:
                return visitor.visitChildren(self)


    class ExplicitFunctionalContext(FunctionalContext):

        def __init__(self, parser, ctx): # actually a QueryParser.FunctionalContext)
            super(QueryParser.ExplicitFunctionalContext, self).__init__(parser)
            self.copyFrom(ctx)

        def ExplicitRegex(self):
            return self.getToken(QueryParser.ExplicitRegex, 0)

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterExplicitFunctional(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitExplicitFunctional(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitExplicitFunctional(self)
            else:
                return visitor.visitChildren(self)



    def functional(self):

        localctx = QueryParser.FunctionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functional)
        self._la = 0 # Token type
        try:
            self.state = 144
            token = self._input.LA(1)
            if token in [QueryParser.ExplicitRegex]:
                localctx = QueryParser.ExplicitFunctionalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(QueryParser.ExplicitRegex)

            elif token in [QueryParser.Symbol]:
                localctx = QueryParser.ImplicitFunctionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(QueryParser.Symbol)

            elif token in [QueryParser.Digits]:
                localctx = QueryParser.ImplicitFunctionalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(QueryParser.Digits)

            elif token in [QueryParser.T__7]:
                localctx = QueryParser.ListFunctionalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 115
                self.match(QueryParser.T__7)
                self.state = 117
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 116
                    self.ws()


                self.state = 119
                self.functional()
                self.state = 121
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 120
                    self.ws()


                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 123
                        self.match(QueryParser.T__8)
                        self.state = 125
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                            self.state = 124
                            self.ws()


                        self.state = 127
                        self.functional() 
                    self.state = 132
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 134
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 133
                    self.ws()


                self.state = 137
                _la = self._input.LA(1)
                if _la==QueryParser.T__8:
                    self.state = 136
                    self.match(QueryParser.T__8)


                self.state = 140
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 139
                    self.ws()


                self.state = 142
                self.match(QueryParser.T__9)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Symbol(self):
            return self.getToken(QueryParser.Symbol, 0)

        def getRuleIndex(self):
            return QueryParser.RULE_identifier

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterIdentifier(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitIdentifier(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = QueryParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(QueryParser.Symbol)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BackReferenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.BackReferenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(QueryParser.NumberContext,0)


        def getRuleIndex(self):
            return QueryParser.RULE_backReference

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterBackReference(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitBackReference(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitBackReference(self)
            else:
                return visitor.visitChildren(self)




    def backReference(self):

        localctx = QueryParser.BackReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_backReference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(QueryParser.T__10)
            self.state = 149
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuantifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.QuantifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QueryParser.RULE_quantifier

     
        def copyFrom(self, ctx):
            super(QueryParser.QuantifierContext, self).copyFrom(ctx)



    class Quantifier0toNContext(QuantifierContext):

        def __init__(self, parser, ctx): # actually a QueryParser.QuantifierContext)
            super(QueryParser.Quantifier0toNContext, self).__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(QueryParser.NumberContext,0)

        def ws(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.WsContext)
            else:
                return self.getTypedRuleContext(QueryParser.WsContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterQuantifier0toN(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitQuantifier0toN(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitQuantifier0toN(self)
            else:
                return visitor.visitChildren(self)


    class QuantifierNContext(QuantifierContext):

        def __init__(self, parser, ctx): # actually a QueryParser.QuantifierContext)
            super(QueryParser.QuantifierNContext, self).__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(QueryParser.NumberContext,0)

        def ws(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.WsContext)
            else:
                return self.getTypedRuleContext(QueryParser.WsContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterQuantifierN(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitQuantifierN(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitQuantifierN(self)
            else:
                return visitor.visitChildren(self)


    class QuantifierZeroOrOneContext(QuantifierContext):

        def __init__(self, parser, ctx): # actually a QueryParser.QuantifierContext)
            super(QueryParser.QuantifierZeroOrOneContext, self).__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterQuantifierZeroOrOne(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitQuantifierZeroOrOne(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitQuantifierZeroOrOne(self)
            else:
                return visitor.visitChildren(self)


    class QuantifierNtoMContext(QuantifierContext):

        def __init__(self, parser, ctx): # actually a QueryParser.QuantifierContext)
            super(QueryParser.QuantifierNtoMContext, self).__init__(parser)
            self.copyFrom(ctx)

        def number(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.NumberContext)
            else:
                return self.getTypedRuleContext(QueryParser.NumberContext,i)

        def ws(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(QueryParser.WsContext)
            else:
                return self.getTypedRuleContext(QueryParser.WsContext,i)


        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterQuantifierNtoM(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitQuantifierNtoM(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitQuantifierNtoM(self)
            else:
                return visitor.visitChildren(self)



    def quantifier(self):

        localctx = QueryParser.QuantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_quantifier)
        self._la = 0 # Token type
        try:
            self.state = 194
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                localctx = QueryParser.QuantifierZeroOrOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(QueryParser.T__11)
                pass

            elif la_ == 2:
                localctx = QueryParser.QuantifierNContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(QueryParser.T__12)
                self.state = 154
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 153
                    self.ws()


                self.state = 156
                self.number()
                self.state = 158
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 157
                    self.ws()


                self.state = 160
                self.match(QueryParser.T__13)
                pass

            elif la_ == 3:
                localctx = QueryParser.QuantifierNtoMContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(QueryParser.T__12)
                self.state = 164
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 163
                    self.ws()


                self.state = 166
                self.number()
                self.state = 168
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 167
                    self.ws()


                self.state = 170
                self.match(QueryParser.T__8)
                self.state = 172
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 171
                    self.ws()


                self.state = 174
                self.number()
                self.state = 176
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 175
                    self.ws()


                self.state = 178
                self.match(QueryParser.T__13)
                pass

            elif la_ == 4:
                localctx = QueryParser.Quantifier0toNContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.match(QueryParser.T__12)
                self.state = 182
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 181
                    self.ws()


                self.state = 184
                self.match(QueryParser.T__8)
                self.state = 186
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 185
                    self.ws()


                self.state = 188
                self.number()
                self.state = 190
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QueryParser.WhiteSpace) | (1 << QueryParser.BlockComment) | (1 << QueryParser.LineComment))) != 0):
                    self.state = 189
                    self.ws()


                self.state = 192
                self.match(QueryParser.T__13)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Digits(self):
            return self.getToken(QueryParser.Digits, 0)

        def getRuleIndex(self):
            return QueryParser.RULE_number

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitNumber(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = QueryParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(QueryParser.Digits)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(QueryParser.WsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WhiteSpace(self, i=None):
            if i is None:
                return self.getTokens(QueryParser.WhiteSpace)
            else:
                return self.getToken(QueryParser.WhiteSpace, i)

        def BlockComment(self, i=None):
            if i is None:
                return self.getTokens(QueryParser.BlockComment)
            else:
                return self.getToken(QueryParser.BlockComment, i)

        def LineComment(self, i=None):
            if i is None:
                return self.getTokens(QueryParser.LineComment)
            else:
                return self.getToken(QueryParser.LineComment, i)

        def getRuleIndex(self):
            return QueryParser.RULE_ws

        def enterRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.enterWs(self)

        def exitRule(self, listener):
            if isinstance( listener, QueryListener ):
                listener.exitWs(self)

        def accept(self, visitor):
            if isinstance( visitor, QueryVisitor ):
                return visitor.visitWs(self)
            else:
                return visitor.visitChildren(self)




    def ws(self):

        localctx = QueryParser.WsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ws)
        try:
            self.state = 213
            token = self._input.LA(1)
            if token in [QueryParser.WhiteSpace]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 198
                        self.match(QueryParser.WhiteSpace)

                    else:
                        raise NoViableAltException(self)
                    self.state = 201 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)


            elif token in [QueryParser.BlockComment]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 203
                        self.match(QueryParser.BlockComment)

                    else:
                        raise NoViableAltException(self)
                    self.state = 206 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)


            elif token in [QueryParser.LineComment]:
                self.enterOuterAlt(localctx, 3)
                self.state = 209 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 208
                        self.match(QueryParser.LineComment)

                    else:
                        raise NoViableAltException(self)
                    self.state = 211 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




