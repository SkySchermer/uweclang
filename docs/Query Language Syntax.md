
# Query Syntax Help

### Comments

Comments can be inserted into the query using two different comment notations:

```
// This is a line comment. Any text on this line after the '//' symbol is ignored.

/*
   This is a block comment. 
   These comments can span multiple lines.
 */ 
```


### Literal Matches

To match a literal word or an exact sequence of words, just type type the words to match:

```
// This will match an exact sequence of words:

she visited the bank;

// The matched words are separated by whitespace, so you can arrange them vertically at your convenience:

// An equivalent query:
    she
    visited
    the
    bank
```

Note the semicolon (`;`): this character is used to separate distinct queries. It is not required on the last query.


### Regular Expressions

Literal matches and match functions employ [Python Regular Expressions](https://docs.python.org/2/library/re.html#regular-expression-syntax). 

```
"This is a regular expression"
".*"        // matches anything
"..."       // matches any three letter word
"{gu}(2,3)" // matches 'gugu' and 'gugugu'
"h[ao]t"    // matches 'hot' and 'hat'
```


### Match Functions

The colon (`:`) character is used to invoke a `match function`. The default behavior of the match function is to perform a match on the result of another match.

```
// This will match the words starting with "she":
    she.*

// This will match the words ending with "'s":
    .*'s

// We can match both at the same time (words starting with "she" that end with "'s") by using the default match function:
    she.*:.*'s

// This example is a little contrived, because there is a more straightforward way of making this query:
    she.*'s

// However, you might consider using the match function with match definitions. 
```

Alternate behaviors of the match function can be invoked by naming a built-in function:
```
// This will match any noun:
    .*:tag:n.*

// The initial ".*" will match any word, then the ":tag" match function will extract the tag of that word, then the ":n.*" default match function will match only tags starting with "n".

// Furthermore, if a match function is supplied without a given literal to match, an implicit ".*" is provided. Thus, the above qury can be simplified:
    :tag:n.*
```



### Quoting
In order to match text that includes special characters used by the query language, you can quote the match pattern:

```
// This will match a semicolon:
    ";"

// Becase the quoted text is a regular expression, regular expression symbols will need to be escaped.

// This will match a period:
    "\."

// This will match a double quote:
    "\""

```


### Or-Match
Matching one or more of a set of options is builtin to the regular expression syntax.

```
// This will match any of four different phrases:
    he|she
    visited
    the
    bank|store

// he visited the bank
// he visited the store
// she visited the bank
// she visited the store
```


### Intersection Match
Matching a word that must meet two conditions requires the match function. The default match function will match against the result of the previous match:

```
// Matches any word starting with "s" and ending with "'s":
    s.*:.*'s

// To match against a word and a tag, the tag match function can be used:
// Matches any word "hit" used as a noun:
    hit:tag:n.*

```


### Negated Match

To negate a match, use the `~` symbol:

```
// Matches any word except 'button':
    ~button

// Matches any word not tagged 'NNP':
    .*:tag:~NNP
```


### Backreference

A backreference will require that the word match a previous word exactly.

```
// This will match "The a a" where 'a' is any word.
    the
    .*
    \2
```

Backreferences only work in the first position, not after a match function `:`.


### Match Definitions

Subqueries can be defined for convenience in writing complex queries. This allows you to match against a list of words using another name:

```
define ADDITIVE_ADVERB [
    additionally,
    also,
    alternatively,
    further,
    furthermore,
    likewise,
    moreover,
    namely,
    similarly,
];

define LINKING_TRIGRAM [
    all things considered,
    as a consequence,
    as a result,
    in that case,
]

// Finds all additive adverbs with following commas and linking trigrams:
    ADDITIVE_ADVERB 
    "," 
    LINKING_TRIGRAM

```


