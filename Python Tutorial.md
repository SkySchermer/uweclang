
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
  + [Ranges and Enumeration](#ranges-and-enumeration)
  + [Dictionaries](#dictionaries)
  + [Args & Kwargs](#args--kwargs)
  + [Objects](#Objects)
  + [Regular Expressions](#regular-expressions)


Python Features
---------------

This section contains an introduction to many of the basic features fo the Python language. It focuses mainly on the syntax of common, generally applicable constructs.


### Docstrings

Python provides a built-in means of documenting functions, objects, and packages using *docstrings*. A docstring is a string that is provided on the first line of an object, and not explicitly assigned to anything. A docstring for a function looks like this:

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

Lists are a means of assinging a name to a collection of data. They are probably the most commonly used kind of object in Python (aside from [dictionaries](#dictionaries)). To create a list:

```python
my_empty_list = []
another_way_list = list()
my_list_of_items = [1, 2, 3, 'item4', 5.5, [], False, (1, 2)]
```

Notice that lists can contain just about anything, including other lists.
To find the length of a list use the built-in [`len`](https://docs.python.org/3/library/functions.html#len) function:

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

Tuples are also useful with the 'splat' or 'pack/unpack' operator `*`, as described [below](#args--kwargs).


### Format Strings

There are two basic ways of displaying formatted output in Python. The first is to manually `print` how you want it:

```python
number = 3.4
print('The number is', number, '.')
```

By default, the arguments to `print` are seperated using spaces, which makes the output look like so:

```
the number is 3.4 .
```

This can be fixed by configuring the [print seperator](https://docs.python.org/3.4/library/functions.html#print), but there is a simpler, more flexable way to do this kind of thing:

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

The name `arg2` is only bound inside the function, even though you use it when calling the function. This may be confusing if you use the same variable names inside and outside:

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

Oftentimes, when operating on lists of data, you don't need access to the whole list at once to produce the results you want. Rather than passing around a whole list of data in memory, you can pass a function that looks up the next value and returns it when requested. *Generators Objects* are objects that implement this behavior.

For instance, in Python 3, if you try to print the results returned by the `map` function, you may get something like `<map object at 0x104ef8358>`. You can convert this to a list by calling `list` on it. In general, you want to avoid converting these objects to lists unless it is really necessary. Rather than converting it to a list, you could write:

```python
for item in map_object:
    print(item)
```

This will preserve the efficiency of the generator object.

You can create your own generators by defining functions using the [`yield`](https://docs.python.org/2/reference/simple_stmts.html#the-yield-statement) statement. You can also use *Generator Comprehensions*, which behave like list comprehensions, but produce a generator object instead of a list:

```python
my_generator = (item for item in my_list if condition)
```

See [here](https://docs.python.org/2/reference/simple_stmts.html#the-yield-statement) for more information.

### Lambda

A *Lambda Expression* is a way to define anonymous functions. They are mostly used to provide simple functions as arguments to other functions like `map` and `filter`. For example, to quickly increment numbers in a list:

```python
result = map(lambda x: x+1, my_list)
```

The lambda defines a function that takes one argument, `x`, and returns `x+1`. 

This style of programming is not common in python. Usually, it is clearer to use a list comprehension, as this avoids the words `map` and `lambda`, which are abstractions that don't have anything to do with the result:

```python
result = [x+1 for x in my_list]
```

However, when passing arguments to functions other than `map` and `filter`, lambdas may be more appropriate.

Note that it is a violation of the [style guide](https://www.python.org/dev/peps/pep-0008/) to directly assign names to lambdas. This defeats the whole point of using them and possibly obfuscates their arguments; just use a `def` statement instead.


### Slices

*Slicing* is a technique for concisely producing subsets of lists and tuples. A slice is a variation of indexing, where you use `:`'s to specify the limits and step of a sublist. The syntax is `my_list[start:end:step]`. Here are some examples:

```python
>>> my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> my_list[3:6]    # Select elements 3 to 6
[4, 5, 6]
>>> my_list[1:8:2]  # Select 1 to 8, stepping by 2
[2, 4, 6, 8]
>>> my_list[1:8:3]  # Select 1 to 8, stepping by 3
[2, 5, 8]
>>> my_list[4:]     # Select from 4 to the end
[5, 6, 7, 8, 9, 0]
>>> my_list[:4]     # Select from the start to 4
[1, 2, 3, 4]
>>> my_list[::2]    # Select from start to end, stepping by 2
[1, 3, 5, 7, 9] 
>>> my_list[::-2]   # Select from start to end, stepping in reverse by 2
[0, 8, 6, 4, 2]
```

Slices work on tuples in the same manner. Note that the slice is inclusive on the start index, but exclusive on the end index. This is to ensure the number of elements selected is equal to the difference `end - start`.


### Dictionaries

Dictionaries are a fundamental part of how python operates. All attributes and underlying mechanics of objects and modules in python are implemented using dictionaries. Fortunately, dictionaries are fairly simple to use.


Dictionaries, like lists and tuples, are a means of assinging a name to a collection of data. Dictionaries map *keys* to *values*, much like a list maps indices to values. To create a dictionary:

```python
my_empty_dict = {}
another_way_dict = dict()
my_dict = {'item1' : 1, 'item2': 2, 3 : [], 4.5 : 'a', True : {}}
```

Dictionaries can contain just about anything as values, but only objects that can be *hashed* are available to be keys: this excludes lists, dictionaries, and other variable-sized objects. You can use tuples, however, since they can't change size.

To access an element of a list, use the `[]` index operator:

```python
>>> my_dict['item1']
1
>>> my_dict[3]
[]
>>> my_dict[True]
{}
```

The `len` function will return the number of entries in the dictionary:

```python
>>> len(my_dict)
5
```

You can check if a key is in the dictionary with the `in` keyword:

```python
if 'item1' in my_dict:
    print('Found item1:', my_dict['item1'])
else:
    print('item1 not found.')
```


For a listing of dictionary functions, see the [documentation](https://docs.python.org/2/library/stdtypes.html#typesmapping).


### Ranges and Enumeration

Oftentimes, you may want to enumerate over some data or perform a task a specific number of times. The [`range`](https://docs.python.org/3/library/functions.html#func-range) built-in function is useful for creating lists of numbers. (In Python 3, it produces a [generator](#generators).) For example, to print a list of 15 numbers, you can do this:

```python
>>> for x in range(0, 15):
...     print(x)
...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
```

(Note that the start value is included and the end value is not -- this will print all numbers 0 to 14.)

If you want to loop over a list and keep track of the current index, you can use the [`enumerate`](https://docs.python.org/3/library/functions.html#enumerate) built-in, which returns the index and value as a tuple:

```python
>>> for i, v in enumerate(['a', 'b', 'c', 'd']): 
...     print(i, v)
...
0 a
1 b
2 c
3 d
```


### Args & Kwargs

The `*` (splat) and `**` (double-splat) operators allow you to 'pack' tuples and dictionaries, which allow you to define functions which can accept any number of arguments. The following function accepts any number of positional arguments:

```python
def my_function(*args):
    print(args)
```

This behaves like so:

```python
>>> my_function(1, 2, 3)
(1, 2, 3)
>>> my_function('a')
('a')
>>> my_function()
()
```

You can make some arguments required by listing them before the `*args` parameter:

```python
def my_function2(arg1, arg2, *args):
    print(arg1, arg2, args)
```

This behaves like so:
```python
>>> my_function2()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: my_function2() missing 2 required positional arguments: 'arg1' and 'arg2'
>>> my_function2(1, 2)
1 2 ()
>>> my_function2(1, 2, 3, 4, 5)
1 2 (3, 4, 5)
```

Similarly, you can use the `**` operator to accept any number of keyword arguments:

```python
def my_function3(**kwargs):
    print(kwargs)
```

This behaves like so:
```python
>>> my_function3(a='test', b='this is also a test')
{'a': 'test', 'b': 'this is also a test'}
```

These arguments don't need to be named `args` and `kwargs`, but it is their conventional name.

For additional info, see the [documentation](https://docs.python.org/2/tutorial/controlflow.html#arbitrary-argument-lists).


### Objects

*Objects* are a fundamental data type in Python -- everything in Python is an object. An object is a collection of state and functions called *member variables* and *methods*, respectively. Collectively, they are called *attributes*. Fully understanding Python objects is an advanced subject, so only the basics will be covered here.

Objects are created using a template called a *class*. The class defines a *constructor method* that creates objects. Here is a simple class definition:

```python
class MyObject:
    """This is a class docstring."""
    def __init__(self, arg1):
        print('In constructor with arg', arg1)
```

This creates a class called `MyObject`, with a docstring and a contstructor method. The constructor must take at least one argument (called `self`, here) which references the object being created. (This argument can be named anything, but 'self' is the conventional name. Note also that [CamelCase](https://en.wikipedia.org/wiki/CamelCase) is conventionally used for class names.)

To create an object we call the constructor using the object's name:

```python
>>> my_object = MyObject(2)
In constructor with arg 2
>>> my_object
<__main__.MyObject object at 0x107b6d7b8>
```

We can define methods in the same manner as the constructor:

```python
class MyObject:
    """This is a class docstring."""
    def __init__(self, arg1):
        print('In constructor with arg', arg1)
    def do_something(self, what_to_do):
        print(self, 'is doing', what_to_do)
```

Note that we must also provide an argument for referencing the target object (`self`, again.) To call the method, we use the `.` (attribute reference) operator:

```python
>>> my_object = MyObject(2)
In constructor with arg 2
>>> my_object.do_something('brave')
<__main__.MyObject object at 0x107b6d8d0> is doing brave
>>>
```

For additional information, see the [documentation](https://docs.python.org/2/tutorial/classes.html).


### Regular Expressions

Todo...