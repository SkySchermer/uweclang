
Python Tutorial
===============

Table of Contents
-----------------

* [Table of Contents](#table-of-contents)
* [Python Features](#python-features)
  + [Docstrings](#docstrings)
  + [Strings](#Strings)
  + [Lists](#lists)
  + [Tuples](#tuples)
  + [Format Strings](#format-strings)
  + [Keyword Arguments](#keyword-arguments)
  + [List Comprehensions](#list-comprehensions)
  + [Generators](#generators)
  + [Map & Filter](#map--filter)
  + [Lambda](#lambda)
  + [Slices](#slices)
  + [Dictionaries](#dictionaries)
  + [Args & Kwargs](#args--kwargs)
  + [Objects](#Objects)
  + [Regular Expressions](#regular-expressions)


Python Features
---------------

This section contains an introduction to many of the basic features fo the Python language. It focuses mainly on the syntax of common, generally applicable constructs.

### Docstrings

Python provides a builtin means of documenting functions, objects, and packages using *docstrings*. A docstring is a string that is provided on the first line of an object, and not explicitly assigned to anything. A docstring for a function looks like this:

```python
def my_function(args):
    """This is a docstring!"""
    return args
```

(Triple quotes are not necessary, but they are conventionally used for ease of expansion.)

Docstrings for modules are provided on the first line of the module file. Docstrings for packages are provided on the first line of the `__init__.py` file.

To read a docstring you can use the builtin `help` function, or access it directly as an attribute:
```python
help(my_function)
```
```python
myfunction.__doc__
```

For additional information see [PEP-257](https://www.python.org/dev/peps/pep-0257/).

### Strings

Python allows for a number of different syntax styles for representing text data. Below is a summary of the common ones.

* Normal Strings
    ```python
    'This is a string.'
    
    "This is also a string."
    
    "This string 'contains' a quote."
    
    'This one "also" contains a quote.'
    ```

* Mulitline Strings
    ```python
    '''This string
       takes up multiple lines.'''
    
    """So does 
       this one."""

    ('This one is written out on multiple lines' ## <- No comma here!
     ' but the two strings will be joined together as one!')
    ```

* Escape Sequences
    ```python
    'Escape sequences \'allow\' you to embed special characters in a string.'

    #Common escape sequences:
    '\n' ## Newline
    '\r' ## Carriage return (\r\n is how new lines are handled on Microsoft Windows.)
    '\t' ## Tab
    '\'' ## Single quote
    '\"' ## Double quote
    '\0' ## Null character
    '\x00' ## Special character selected by numerical code
    ```

* Raw strings
    ```python
    r'Raw strings allow you to ignore certain escape sequences.'
    r"These are represented directly: \n, \r, \t, \0, etc."
    r'This doesn\'t work on quotes, because they are needed to terminate the string.'

    ```
    
    (Raw strings are very useful for working with [Regular Expressions](#regular-expressions).)

### Lists

Lists are a means of assinging a name to a collection of data. They are probably the most commonly used kind of object in Python. To create a list:

```python
my_empty_list = []
another_way_list = list()
my_list_of_items = [1, 2, 3, 'item4', 5.5, [], False, (1, 2)]
```

Notice that lists can contain just about anything, including other lists.
To find the length of a list use the builtin `len` function:

```python
>>> len(my_list_of_items)
8
>>> len([])
0
>>> len([[]])
1
```

To access an element of a list, use the `[]` index operator:

```python
>>> my_list_of_items[3]
'item4'
```

Notice that the list indexes start at 0, not at 1. (This is to allow easy calculations of list size & positional differences.)

For a listing of list functions, see the [documentation](https://docs.python.org/2.7/tutorial/datastructures.html).

### Tuples

Tuples behave much like lists in that they are collections of data. To create a tuple:

```python
my_empty_tuple = ()
another_way_tuple = tuple()
my_tuple = (1, 2, 3, 'item4', 5.5, [], False, (1, 2))
```

In fact, it is easy to convert between the two:
```python
>>> tuple([1, 2, 'a'])
(1, 2, 'a')
>>> list((1, 2, 'a'))
[1, 2, 'a']
```

They an be indexed the same way:

```python
>>> my_tuple[3]
'item4'
```

But that is about where the similarities end. Tuples cannot change length like lists can, so many of the functions available to lists are not available to tuples. They also have additional functionality called 'unpacking':

```python
>>> (a, b) = (1, 2)
>>> a
1
>>> b
2
```

This allows for conveniently returning mulitple values from a function, for instance. Note that the parenthesis around are not necessary in this pattern:

```python
>>> a, b = 1, 2
```

Tuples are also useful with the 'splat' or 'unpack' operator `*`, as described [below](#args--kwargs).

### Format Strings

There are two basic ways of displaying formatted output in Python. The first is to manually `print` how you want it:

```python
number = 3.4
print('The number is', number, '.')
```

By default, the arguments to `print` are seperated using spaces, which makes the output look like `the number is 3.4 .`. This can be fixed by configuring the print seperator, but there is a simpler, more flexable way to do this kind of thing:

```python
number = 2.3
print('The number is {}.'.format(number))
```

This will insert the number at the `{}` symbol. You can provide indices in the brackets to print something multiple times:

```python
>>> print('{0} {1} {0} {2}'.format('a', 'b', 'c'))
a b a c
```

You can also use floating-point format specifiers to deal with decimal digits easily:

```python
>>> print('{:.2f}, {:.4f}, {:.0f}'.format(1.34343434343, 1.34343434343, 3.555))
1.34, 1.3434, 4
```

The documentation of format strings can be found [here](https://docs.python.org/2/library/string.html#format-string-syntax).

### Keyword Arguments

Keyword arguments allow you to provide default values to functions and simplify how they are used. To define a keyword argument:

```python
def myfunction(arg1, arg2='default value'):
    print(arg1, arg2)
```

The argument arg2 is a keyword argument. Thus we can call the function in multiple ways:

```python
>>>  myfunction(5)
5 'default value'
>>>  myfunction(5, arg2='new value')
5 'new value'
```

The name `arg2` is only bound inside the function, even though you use it when calling the function. This might be confusing if you use the same variable names inside and outside:
```python
>>> arg2 = 'my arg2 value'
>>> myfunction(5, arg2=arg2)
5 'my arg2 value'
```

### List Comprehensions

List comprehesions are the idiomatic way to generate lists and perform [map and filter](#map--filter) operations on data. They essentially operate like `for` loops, but they will always return a list:

```python
>>> myitems = [1, 3, 5, 8]
>>> [x+1 for x in myitems]
[2, 4, 6, 9]
>>> [x+1 for x in myitems if x < 4]
[2, 4]
```

### Map & Filter

The `map` and `filter` functions are a more functional-based way of applying functions to lists. If we have a few functions we with to apply to data:

```python
def increment(x):
    return x+1

def is_small(x):
    return x < 4
```

We can achieve the same results as the list comprehension by using `map` and `filter`:

```python
>>> myitems = [1, 3, 5, 8]
>>> list(map(increment, myitems))
[2, 4, 6, 9]
>>> list(map(increment, filter(is_small, myitems)))
[2, 4]
```

(Note: In Python 3, these functions return [generator objects](#generators), so you'll need to use `list()` to convert them into lists for printing.)

### Generators

Todo...

### Lambda

Todo...

### Slices

Todo...

### Dictionaries

Todo...

### Args & Kwargs

Todo...

### Objects

Todo...

### Regular Expressions

Todo...