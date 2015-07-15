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

* The [uweclang](uweclang) folder is an example of a python package. This folder contains an [__init__.py](#uweclang/__init__.py) file that specifies what modules to import. It also provides detailed information about the package. 

* Note that the particular way the `from _ import` statements are used allows the module functions to be used with shorter qualifications. E.g., `uweclang.x()` instead of `uweclang.batch.tools.x()`. This is not normal! This will cause problems if you have modules with attributes that have the same name.

### Verbosity

Whever a script or function uses a verbosity option, they can be interpreted as follows:

| level | flag | Result                         |
|:-----:|------|--------------------------------|
| 0     | -q   | No output                      |
| 1     | -v   | Completed task output          |
| 2     | -vv  | Resource access/subtask output |
| 3     | -vvv | Excessive output               |

### Code Examples

#### Main

The following code is a common pattern in Python scripts:

```python
if __name__ == '__main__':
```

(As seen in [extract](scripts/extract).)

The purpose of this code is to determine if the script is being run as an executable or imported as a script. Since Python is a dynamic, interpretted language, statements such as defining functions and classes happen when the code is being executed, so importing a script will cause it to run.

This pattern is useful to guard code that shouldn't run when the file is imported.

#### X = X or Y

```python
selector_function = selector_function or (lambda x,y: True)
```

(As seen in [uweclang/plain/plain.py](uweclang/plain/plain.py))

The purpose of this code is to assign a value to selector_function in case one was not provided. This is different from using a default argument, because if the caller explicitly passes `None`, the function will still be assigned. This exploits two features of python:

  * Most objects can be used in boolean expressions, even if they aren't boolean. Some objects have a 'truthy' value. Here, any of `[]`, `''`, `False`, `0`, etc., will all cause the function to assign.

  * The `or` operator is *short circuited*. If the first item on the left evaluates to something truthy, then the item on the right is never evaluated at all. (Conversely, the `and` operator short circuits when a false value is evaluated.)
  

#### Argument Unpacking

```python
[x[0] for x in seperated_text if selector_function(*x)]
```

(As seen in [uweclang/plain/plain.py](uweclang/plain/plain.py).)

In this example, `seperated_text` is a list of tuples, so the each `x` is a tuple. The `*` operator 'unpacks' the tuple, allowing its components to be passed as arguments to the function. So this code is equivalent to the following:

```python
[x[0] for x in seperated_text if selector_function(x[0], x[1])]
```

If we just passed `x` to the function directly, it would be passing a tuple to the first argument, rather than the contents of the tuple to each argument.

A similar thing can be achieved by unpacking dictionaries into keyword arguments using the double-splat operator `**`. See [Args & Kwargs](Python Tutorial.md#args--kwargs) for the reverse operation.