Developer Notes
===============

Table of Contents
-----------------

* [Table of Contents](#table-of-contents)
* [Student Corpus Scripts](#student-corpus-scripts)
  + [Command Line Arguments](#command-line-arguments)
* [UWEC Language Tools package](#uwec-language-tools-package)
  + [Packages, Modules, and Imports](#packages-modules-and-imports)
  + [File Headers](#file-headers)
* [Python Versions](#python-versions)
  + [Shebang](#shebang)
  + [Future Imports](#future-imports)
  + [PYTHONPATH](#pythonpath)
* [Conventions](#conventions)
  + [The Differences Between Scripts, Modules, and Packages](#the-differences-between-scripts-modules-and-packages)
  + [Verbosity](#verbosity)
  + [Python Introduction](#python-introduction)
    * [Docstrings](#docstrings)
    * [Strings](#Strings)
    * [Lists](#lists)
    * [Tuples](#tuples)
    * [Format Strings](#format-strings)
    * [Keyword Arguments](#keyword-arguments)
    * [List Comprehensions](#list-comprehensions)
    * [Generators](#generators)
    * [Map & Filter](#map--filter)
    * [Lambda](#lambda)
    * [Slices](#slices)
    * [Dictionaries](#dictionaries)
    * [Args & Kwargs](#args--kwargs)
    * [Objects](#Objects)
    * [Regular Expressions](#regular-expressions)
  + [Code Examples](#code-examples)
    * [Main](#main)
    * [Tuple Selector](#tuple-selector)
    * [Argument Unpacking](#argument-unpacking)


Student Corpus Scripts
----------------------

### Command Line Arguments

Todo...

https://docs.python.org/3/howto/argparse.html

UWEC Language Tools package
---------------------------

Todo...

### Packages, Modules, and Imports

Todo...

### File Headers

Todo...

Python Versions
---------------

There are many versions of Python, but modern Python mostly fall in two common, major groups: *Python 2* and *Python 3*. Python 3 introduced a number of major non-backward compatable changes into an environment where many people were using Python 2 for a long time. (Many people felt the changes were unnecessary or unwanted.) Because of this, these versions should be considered distinct and somewhat superficially indentical.

On a *nix-like system, you can identify what version you are using by running the following commands:

* `which python` will tell you where your python program is.
* `python --version` will tell you the version number.

If you have Python 3 installed, you may need to use:

* `which python3`
* `python3 --version`

### Shebang

*This section's information may not apply to machines running Microsoft Windows.*

The following pattern is known as a *shebang*:
```python
#! /usr/bin/env python
```

```python
#! /usr/bin/env python3
```

The purpose of this code (which must be at the very top of a script) is to signal to the [shell](https://en.wikipedia.org/wiki/Unix_shell) which program to use to execute the file. The first bit -- `#!` is the shebang. The second bit -- `/usr/bin/env` tells the shell where to find the program. The last bit says which program to use.

Normally, to run a Python script from the command line, you would write something like this:

```shell
python myscript arg1 arg2
```

However, with the shebang, the interpreter knows to use Python, so you can write the following instead:

```shell
./myscript arg1 arg2
```

(This assumes you have permissions for executing the file. You may need to do `chmod +x myscript`.)

### Future Imports

Todo...

### PYTHONPATH

Todo...

Conventions
-----------

### The Differences Between Scripts, Modules, and Packages

A *Python Script* is any file that contains python code. These tend not to have file extensions, since you can invoke them from the command line (using the shebang) more conveniently and idiomatically without it.

* The [extract](scripts/extract) file is a good example of a script. It defines a function `extract_plaintext_from_docx` that is meant to be used internally, then, if run as an executable, it performs its tasks. 

* Notice that the [`__name__ == '__main__'`](#main) is unnecessary here: it is only used to ensure that if (for some strange reason -- maybe the `extract_plaintext_from_docx` is useful elsewhere) the the script is able to be imported without having to do everything else.

A *Python Module* is a python script that is meant to be imported by another script. The line between a script and module is blurry, because by using the [`__name__ == '__main__'`](#main) pattern, you can create scripts that work both as imports and as executables.

* The [docx.py](uweclang/binary/docx.py) file is a good example of a python module. It defines a couple of functions and does nothing else. (If run as an executable, it would load those functions into the interpreter and then quit, and the functions would then unload.) The only way to use these functions is to `import` them. 

* All of the variables, functions, classes, and objects in the module are called 'attributes' of the module. By default, if an attribute name starts with `_`, it will not be available to be imported.

A *Python Package* is a collection of modules. It is useful for grouping a number of modules together under a hierarchical naming scheme. In order to use a package, Python has to know which folders are package folders, and which modules to use. The Python `import` statment will look for `__init__.py` files in folders to determine if they are package folders. (This file doesn't need to have anything in it -- it just has to exist in the right location.) 

* The [uweclang](uweclang) folder is an example of a python package. This folder contains an [__init__.py](#uweclang/__init__.py) files that specifies what modules to import. It also provides detailed information about the package. 

* Note that the particular way the `from _ import` statements are used allows the module functions to be used with shorter qualifications. E.g., `uweclang.x()` instead of `uweclang.batch.tools.x()`. This is not normal! This will cause problems if you have modules with attributes that have the same name.

### Verbosity

Whever a script or function uses a verbosity option, they can be interpreted as follows:

| level | flag | Result                         |
|:-----:|------|--------------------------------|
| 0     | -q   | No output                      |
| 1     | -v   | Completed task output          |
| 2     | -vv  | Resource access/subtask output |
| 3     | -vvv | Excessive output               |

### Python Introduction

This section contains an introduction to many of the basic features fo the Python language. It focuses mainly on the syntax of common, generally applicable constructs.

#### Docstrings

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

#### Strings

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

#### Lists

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

#### Tuples

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

#### Format Strings

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

#### Keyword Arguments

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

#### List Comprehensions

List comprehesions are the idiomatic way to generate lists and perform [map and filter](#map--filter) operations on data. They essentially operate like `for` loops, but they will always return a list:

```python
>>> myitems = [1, 3, 5, 8]
>>> [x+1 for x in myitems]
[2, 4, 6, 9]
>>> [x+1 for x in myitems if x < 4]
[2, 4]
```

#### Map & Filter

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

#### Generators

Todo...

#### Lambda

Todo...

#### Slices

Todo...

#### Dictionaries

Todo...

#### Args & Kwargs

Todo...

#### Objects

Todo...

#### Regular Expressions

Todo...

### Code Examples

##### Main

The following code is a common pattern in Python scripts:

```python
if __name__ == '__main__':
```

(As seen in [extract](scripts/extract).)

The purpose of this code is to determine if the script is being run as an executable or imported as a script. Since Python is a dynamic, interpretted language, statements such as defining functions and classes happen when the code is being executed, so importing a script will cause it to run.

This pattern is useful to guard code that shouldn't run when the file is imported.

##### Tuple Selector

```python
for x in targets:
    (ignored_files, files)[file_selector(x)].append(x)
```

(As seen in [uweclang/batch/tools.py](uweclang/batch/tools.py).)

This is a fancy way of partitioning a list into two lists based on a predicate. The normal (less efficient, but more readable) way of doing this looks like so:

```python
ignored_files = [x for x in targets if not file_selector(x)]
files         = [x for x in targets if     file_selector(x)]
```

Or, alternatively (equally efficient, but more verbose):

```python
for x in targets:
    if file_selector(x):
        files.append(x)
    else:
        ignored_files.append(x)
```

This pattern exploits a quirk of python that allows `True` to act like `1`, and `False` to act like `0`. So we take the tuple `(ignored_files, files)`, and take the first item if `is_valid_target(x)` evaluates to false, and the second otherwise. Then we call the `.append()` method on `x` to add it to the selected list

##### Argument Unpacking

```python
[x[0] for x in seperated_text if selector_function(*x)]
```

(As seen in [uweclang/plain/student.py](uweclang/plain/student.py).)

In this example, `seperated_text` is a list of tuples, so the each `x` is a tuple. The `*` operator 'unpacks' the tuple, allowing its components to be passed as arguments to the function. So this code is equivalent to the following:

```python
[x[0] for x in seperated_text if selector_function(x[0], x[1])]
```

If we just passed `x` to the function directly, it would be passing a tuple to the first argument, rather than the contents of the tuple to each argument.

A similar thing can be achieved by unpacking dictionaries into keyword arguments using the double-splat operator `**`. See [Args & Kwargs](#args--kwargs) for the reverse operation.