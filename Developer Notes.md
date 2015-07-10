Developer Notes
===============

Table of Contents
-----------------

* [Table of Contents](#table-of-contents)
* [Student Corpus Scripts](#student-corpus-scripts)
  * [Command Line Arguments](#command-line-arguments)
* [UWEC Language Tools package](#uwec-language-tools-package)
  * [Packages, Modules, and Imports](#packages-modules-and-imports)
  * [File Headers](#file-headers)
* [Python Versions](#python-versions)
  * [Shebang](#shebang)
  * [Future Imports](#future-imports)
  * [PYTHONPATH](#pythonpath)
* [Conventions](#conventions)
  * [The Differences Between Scripts, Modules, and Packages](#the-differences-between-scripts-modules-and-packages)
  * [Verbosity](#verbosity)
  * [Python Introduction](#python-introduction)
    * [Docstrings](#docstrings)
    * [Lists](#lists)
    * [Tuples](#tuples)
    * [Format Strings](#format-strings)
    * [Keyword Arguments](#keyword-arguments)
    * [List Comprehensions](#list-comprehensions)
    * [Generators](#generators)
    * [Map & Filter](#map--filter)
    * [Sections](#sections)
    * [Dictionaries](#dictionaries)
    * [Regular Expressions](#regular-expressions)
  * [Code Examples](#code-examples)
    * [Main](#main)
    * [Tuple Selector](#tuple-selector)


Student Corpus Scripts
----------------------

## Command Line Arguments

UWEC Language Tools package
---------------------------

## Packages, Modules, and Imports

## File Headers

Python Versions
---------------

There are many versions of Python, but modern Python mostly fall in two common, major groups: *Python 2* and *Python 3*. Python 3 introduced a number of major non-backward compatable changes into an environment where many people were using Python 2 for a long time. (Many people felt the changes were unnecessary or unwanted.) Because of this, these versions should be considered distinct and somewhat superficially indentical.

On a *nix-like system, you can identify what version you are using by running the following commands:

* `which python` will tell you where your python program is.
* `python --version` will tell you the version number.

If you have Python 3 installed, you may need to use:

* `which python3`
* `python3 --version`

## Shebang

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

## Future Imports


## PYTHONPATH



Conventions
-----------

## The Differences Between Scripts, Modules, and Packages

A *Python Script* is any file that contains python code. These tend not to have file extensions, since you can invoke them from the command line (using the shebang) more conveniently and idiomatically without it.

* The [extract](scripts/extract) file is a good example of a script. It defines a function `extract_plaintext_from_docx` that is meant to be used internally, then, if run as an executable, it performs its tasks. 

* Notice that the [`__name__ == '__main__'`](#main) is unnecessary here: it is only used to ensure that if (for some strange reason -- maybe the `extract_plaintext_from_docx` is useful elsewhere) the the script is able to be imported without having to do everything else.

A *Python Module* is a python script that is meant to be imported by another script. The line between a script and module is blurry, because by using the [`__name__ == '__main__'`](#main) pattern, you can create scripts that work both as imports and as executables.

* The [docx.py](uweclang/binary/docx.py) file is a good example of a python module. It defines a couple of functions and does nothing else. (If run as an executable, it would load those functions into the interpreter and then quit, and the functions would then unload.) The only way to use these functions is to `import` them. 

* All of the variables, functions, classes, and objects in the module are called 'attributes' of the module. By default, if an attribute name starts with `_`, it will not available to be imported.

A *Python Package* is a collection of modules. It is useful for grouping a number of modules together under a hierarchical naming scheme. In order to use a package, Python has to know which folders are package folders, and which modules to use. The Python `import` statment will look for `__init__.py` files in folders to determine if they are package folders. (This file doesn't need to have anything in it -- it just has to exist in the right location.) 

* The [uweclang](uweclang) folder is an example of a python package. This folder contains an [__init__.py](#uweclang/__init__.py) files that specifies what modules to import. It also provides detailed information about the package. 

* Note that the particular way the `from _ import` statements are used allows the module functions to be used with shorter qualifications. E.g., `uweclang.x()` instead of `uweclang.batch.tools.x()`. This is not normal! This will cause problems if you have modules with attributes that have the same name.

## Verbosity

Whever a script or function uses a verbosity option, they can be interpreted as follows:

| level | flag | Result                         |
|:-----:|------|--------------------------------|
| 0     | -q   | No output                      |
| 1     | -v   | Completed task output          |
| 2     | -vv  | Resource access/subtask output |
| 3     | -vvv | Excessive output               |

## Python Introduction

### Docstrings
### Lists
### Tuples
### Format Strings
### Keyword Arguments
### List Comprehensions
### Generators
### Map & Filter
### Sections
### Dictionaries
### Regular Expressions

## Code Examples

#### Main

The following code is a common pattern in Python scripts:

```python
if __name__ == '__main__':
```

(As seen in [extract](scripts/extract))

The purpose of this code is to determine if the script is being run as an executable or imported as a script. Since Python is a dynamic, interpretted language, statements such as defining functions and classes happen when the code is being executed, so importing a script will cause it to run.

This pattern is useful to guard code that shouldn't run when the file is imported.

#### Tuple Selector

```python
for x in targets:
    (ignored_files, files)[is_valid_target(x)].append(x)
```

(As seen in [extract](scripts/extract))

This is a fancy way of partitioning a list into two lists based on a predicate. The normal (less efficient, but more readable) way of doing this looks like so:

```python
ignored_files = [x for x in targets if not is_valid_target(x)]
files         = [x for x in targets if     is_valid_target(x)]
```

Or, alternatively (equally efficient, but more verbose):

```python
for x in targets:
    if is_valid_target(x):
        files.append(x)
    else:
        ignored_files.append(x)
```

This pattern exploits a quirk of python that allows `True` to act like `1`, and `False` to act like `0`. So we take the tuple `(ignored_files, files)`, and take the first item if `is_valid_target(x)` evaluates to false, and the second otherwise. Then we call the `.append()` method on `x` to add it to the selected list