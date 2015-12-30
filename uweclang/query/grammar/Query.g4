
grammar Query;

queryDocument
    : (ws? documentItem ws? (';' | EOF) ws?)*
    ;

documentItem
    : query                               # QueryStatement
    | 'define' ws identifier ws query ws? # Definition
    ;

// Represents a full block of text to search for.
query
    : termNegatable (ws termNegatable)*
    ;

// Represents a possibly negated query item.
termNegatable
    : '~' term # NegativeTerm
    | term     # PositiveTerm
    ;

// Represents a search for a subset of the query text.
term
    : '(' query ')' quantifier?           # SubQueryTerm
    | matchFunction                       # SimpleTerm
    | matchFunction ('::' matchFunction)+ # IntersectionTerm
    ;

// Specifies the functions to run on the text token.
matchFunction
    : (':' functionalNegatable)+                     # DirectApply
    | functionalNegatable (':' functionalNegatable)* # MatchApply
    | backReference (':' functionalNegatable)*       # BackReferenceApply
    ;

functionalNegatable
    : '~' functional # NegativeFunctional
    | functional     # PositiveFunctional
    ;

// Represents a regex or the name of a function.
functional
    : ExplicitRegex # ExplicitFunctional
    | Symbol        # ImplicitFunctional
    | Digits        # ImplicitFunctional
    | '[' ws? functional ws? (',' ws? functional)* ws? ','? ws? ']' 
                    # ListFunctional
    ;

identifier
    : Symbol
    ;

backReference
    : '\\' number
    ;

// Quantifiers for repeated token searches.
quantifier
    : '?'                                        # QuantifierZeroOrOne
    | '{' ws?  number ws? '}'                    # QuantifierN
    | '{' ws?  number ws? ',' ws? number ws? '}' # QuantifierNtoM
    | '{' ws? ',' ws?  number ws? '}'            # Quantifier0toN
    // Infinite quantifiers
    //| '*'
    //| '+'
    //| '{' ws? number ws? ',' ws? '}'
    ;

// An integer.
number 
    : Digits
    ;

// Whitespace or comments.
ws
    : WhiteSpace+
    | BlockComment+
    | LineComment+
    ;

// Represents a regex explicitely delimitted by quotes. This allows
// whitespace and special chars to be caputured in the match.
ExplicitRegex
    : '"' (ESCAPED_CHAR | NON_QUOTE)* '"'
    ;

Digits
    : DIGIT
    | NONZERO_DIGIT DIGIT*
    ;

// Represents a function name, or if no function has that name, a regex.
Symbol
    : SYMBOL_CHAR+
    ;

// Whitespace.
WhiteSpace 
    : (' ' | '\t' | '\r' | '\n');

NewLine
    : '\r'? '\n'
    ;

// C-style block comment. Skipped.
BlockComment
    : '/*' .*? '*/'
    -> skip;

// C-style line comment. Skipped.
LineComment
    : '//' ~[\r\n]*
    -> skip;

fragment DIGIT         : '0'..'9';
fragment NONZERO_DIGIT : '1'..'9';
fragment NON_QUOTE     : ~('"');
fragment WHITESPACE    : ' ' | '\t' | '\r' | '\n';
fragment SYMBOL_CHAR   : ~
                       ( ':' | '~'
                       | ' ' | '\t' | '\r' | '\n'  
                       | '"' 
                       | '/' | '\\'
                       | '(' | ')'
                       | '{' | '}'
                       | '[' | ']'
                       | ',' | ';')
                       ;
fragment ESCAPED_CHAR  : '\\\"' 
                       | '\\\\'
                       ;

// antlr4 -Dlanguage=Python2 -visitor Query.g4