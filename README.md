UWEC Language Tools
===================

### Table of Contents
* [UWEC Language Tools](#uwec-language-tools)
	* [Table of Contents](#table-of-contents)
	* [Introduction](#introduction)
	* [Student Corpus Scripts](#student-corpus-scripts)
		* [Pipeline](#pipeline)
		* [Intermediate Files](#intermediate-files)
	* [Available Functions](#available-functions)
	* [Additional Resources](#additional-resources)

### Introduction

This project houses a number of python scripts for analyzing student paper corpora. It is meant to be used in conjunction with [NLTK][nltk.org]. This repository calssifies scripts into two major categories:

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

  It is important to note that this import will only work if the [uweclang](uweclang) folder is in PYTHONPATH. The simplest (and least flexible) way to do this is to put the [uweclang](uweclang) folder in the current directory when running scripts. (On *nix-like systems, you may need to run `export PYTHONPATH=.` first.)

There is an additional [misc](scripts/misc) folder that contains older scripts for reference.


Student Corpus Scripts
----------------------

The student corpus scripts can each be used on single files or on entire directories. To process a single file use the following syntax:

	script-name file [output_directory]

If the output directory is not supplied, the resulting output will be in the current directory. To process a directory use the following syntax:

	script-name [-b [batch_size]] input_directory output_directory

If the `-b` flag is provided, the output will be subdivided into batch directories, each containing `batch-size` files. (The default batch size is 10.)

For help on a given script, use:

    script-name -h

### Pipeline

The student corpus scripts are meant to be run in sequence to accomplish the following tasks:

* Extract XML from docx files.
* Extract plaintext from XML. (Script: [extract.py](scripts/extract.py))
  - output file.raw.txt
* Process plaintext to extract citations, dates, titles, and writer's memos. (Script: [scrub.py](scripts/scrub.py))
  - output file.txt
  - output file.log
  - output file.memo.txt
* Manually verify each file.
* Tag student files. (Script: [tag.py](scripts/tag.py))
  - output file.tag.txt
* Summarize tagged files. (Script: [summary.py](scripts/summary.py))

### Intermediate Files



* Summer 2015
  + Student Corpus
    * Unprocessed Files
    * Plain Files
    * Processed Files
      - batchXXX
    * Tagged Files

Available Functions
-----------------------------

* uweclang
  + batch
    * [tools](uweclang/batch/tools.py)
      - `BATCH_PARSER`
      - `batch_process(process)`
  + binary
    * [docx](uweclang/binary/docx.py)
      - `get_document_xml(filename)`
      - `xml_to_plain(document)`
  + plain
    * [student](uweclang/plain/student.py)
    * [tools](uweclang/plain/tools.py)
      - `line_split(text)`
  + tagged


Additional Resources
--------------------

* [Natural Language Toolkit][nltk.org]
  - [NLTK book](http://www.nltk.org/book/)
* [Python](https://www.python.org/)
  - [Style Guide](https://www.python.org/dev/peps/pep-0008/)

[nltk.org]: http://www.nltk.org/