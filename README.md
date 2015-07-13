UWEC Language Tools
===================


### Table of Contents
* [UWEC Language Tools](#uwec-language-tools)
  + [Table of Contents](#table-of-contents)
  + [Introduction](#introduction)
  + [Student Corpus Scripts](#student-corpus-scripts)
      - [Examples](#examples)
    * [Pipeline](#pipeline)
    * [Intermediate Files](#intermediate-files)
  + [UWEC Language Tools - Available Functions](#uwec-language-tools---available-functions)
  + [Additional Resources](#additional-resources)

The [Developer Notes](Developer Notes.md) contain a list of programming guidelines for writing scripts. It has basic information about Python, and it is mostly focused on the patterns that are used in this project. The [Python Tutorial](Python Tutorial.md) contains a very rapid introduction to most of Python's common features. It is somewhat of a reference tool.

### Introduction

This project houses a number of python scripts for analyzing student paper corpora. It is meant to be used in conjunction with [NLTK][nltk.org]. This repository classifies scripts into two major categories:

1. Student Corpus scripts

  Student corpus scripts are located in the [scripts](scripts) folder. These are meant to be used to process corpus files in bulk and perform analysis and summaries on the resulting files.

2. UWEC Language Tools package

  The Language Tools package is located in the [uweclang](uweclang) folder. These files are meant to provide common functions for use in writing pipeline scripts. To access the package inside a script, use

  ```python
  import uweclang
  ```

  After doing this, the [functions](#available-functions) will be accessible by prefixing them with the `uweclang` prefix like so:

  ```python
  uweclang.get_document_xml('myfile.docx')
  ```

  It is important to note that this import will only work if the [uweclang](uweclang) folder is in PYTHONPATH. The simplest (and least flexible) way to do this is to ensure the [uweclang](uweclang) folder is in the current directory when running scripts. (On *nix-like systems, you may need to run `export PYTHONPATH=.` first.)

There is an additional [misc](scripts/misc) folder that contains older scripts for reference.


Student Corpus Scripts
----------------------

The student corpus scripts can each be used on single files or on entire directories. To process a single file use the following syntax:

	script-name file -o output_directory

If the output directory is not supplied, the resulting output will be in the current directory. 

For help on a given script, use:

    script-name -h


#### Examples
```shell
scripts/extract "Summer 2015/Student Corpus/Unprocessed Files/" -o "Summer 2015/Student Corpus/Plain Files/" -b 5 -m count
```


### Pipeline

The student corpus scripts are meant to be run in sequence to accomplish the following tasks:

1. Extract plaintext from Word. (Script: [extract](scripts/extract))
  - output: ___.raw.txt
2. Process plaintext to extract citations, dates, titles, and writer's memos. (Script: [scrub](scripts/scrub))
  - output: ___.txt
  - output: ___.log
  - output: ___.memo.txt
3. Manually verify each file.
4. Tag student files. (Script: [tag](scripts/tag))
  - output: ___.tag.txt
5. Summarize tagged files. (Script: [summary](scripts/summary))


### Intermediate Files

* Summer 2015
  + Student Corpus
    * Unprocessed Files
    * Plain Files
    * Processed Files
      - batchXXX
    * Tagged Files


UWEC Language Tools - Available Functions
-----------------------------------------

* uweclang
  + batch
    * [tools](uweclang/batch/tools.py)
      - `BATCH_PARSER`
      - `select_files(args)`
      - `batch_process(process)`
  + binary
    * [docx](uweclang/binary/docx.py)
      - `PlainTextExtractor`
      - `get_document_xml(filename)`
      - `xml_to_plain(document)`
  + plain
    * [student](uweclang/plain/student.py)
      - `punctuation_density(text)`
      - `capitalization_density(text)`
      - `clean_punctuation(text)`
      - `parse_parentheticals(text)`
      - `recombine_parentheticals(parse_tree)`
    * [tools](uweclang/plain/tools.py)
      - `line_split(text)`
  + tagged


Additional Resources
--------------------

* [Natural Language Toolkit][nltk.org]
  - [NLTK book](http://www.nltk.org/book/)
* [Python](https://www.python.org/)
  - [Style Guide](https://www.python.org/dev/peps/pep-0008/)
  - [Regular Expressions](https://docs.python.org/2/howto/regex.html)
    * [Regexr](http://www.regexr.com/) -- helpful tool for building and understanding regex. (This uses JavaScript, so its regular expressions may not behave exactly like python in corner cases.)
    * [Pythex](http://pythex.org/) -- A not-as-good regex tester that uses Python.
  - [Python 2/Python 3 compatability](http://python-future.org/compatible_idioms.html)

[nltk.org]: http://www.nltk.org/