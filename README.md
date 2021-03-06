UWEC Language Tools
===================

This file is meant to be viewed on Github at:
https://github.com/SkySchermer/uweclang

### Table of Contents
* [UWEC Language Tools](#uwec-language-tools)
  + [Table of Contents](#table-of-contents)
  + [Introduction](#introduction)
  + [Student Corpus Scripts](#student-corpus-scripts)
      - [Examples](#examples)
    * [Pipeline](#pipeline)
    * [Intermediate Files](#intermediate-files)
  + [Query Language](#query-language)
  + [Query Website](#query-website)
  + [Python uweclang library - Available Functions](#uweclang-library---available-functions)
  + [Additional Resources](#additional-resources)

The [Developer Notes](docs/Developer Notes.md) contain a list of programming guidelines for writing scripts. It has basic information about Python, and it is mostly focused on the patterns that are used in this project. The [Python Tutorial](docs/Python Tutorial.md) contains a very rapid introduction to most of Python's common features. It is somewhat of a reference tool.

### Introduction

This project houses a number of python scripts for analyzing student paper corpora. It is meant to be used in conjunction with [NLTK][nltk.org], though it currently only uses the NLTK part-of-speech (POS) tagger. There are four different domains of functionality provided by the project:

1. Student Corpus scripts

  Student corpus scripts are located in the [scripts](scripts) folder. These are meant to be used to process corpus files in bulk and perform analysis and summaries on the resulting files. 

  UPDATE (Fall 2015): The [analyze script](script/analyze) was used to generate various statistics for the corpora. Changing the statistics to ask different questions required a familiarity with the script and Python, so in order to make this part more flexible, we've developed a query language and some scripts to read and execute this language. This new method only uses the script 'pipeline' to produce POS tagged files for the corpus.

2. UWEC Language Tools package

  The Language Tools package is located in the [uweclang](uweclang) folder. These files are meant to provide common functions for use in writing pipeline scripts. To access the package inside a script, use

  ```python
  import uweclang
  ```

  After doing this, the [functions](#available-functions) will be accessible by prefixing them with the `uweclang` prefix like so:

  ```python
  uweclang.get_document_xml('myfile.docx')
  ```

  It is important to note that this import will only work if the [uweclang](uweclang) folder is in PYTHONPATH. The simplest (though least flexible) way to do this is to ensure the [uweclang](uweclang) folder is in the current directory when running scripts. (On Unix-like systems, you may need to run `export PYTHONPATH=.` first.)

There is an additional [misc](scripts/misc) folder that contains older scripts for reference.

3. Query Language
  
  The [query language](Docs/Query Language Syntax.md) is used to describe text pattern queries in a student corpus. A [script](scripts/runquery) is provided to load a query file and execute it on the student corpus. The queries can also be run on the query website.

4. Query Website

  The query website is located in the [django](django) directory. 

  UPDATE (Fall 2015): The website requires some additional setup, and the functionality is not complete yet, but it is useable if everything is done correctly. The preffered method to run queries is using the [runquery script](scripts/runquery).

Student Corpus Scripts
----------------------

The student corpus scripts can each be used on single files or on entire directories. To process a single file use the following syntax:

	script-name file -o output_directory

If the output directory is not supplied, the resulting output will be in the current directory. 

For help on a given script, use:

    script-name -h


#### Examples
```shell
scripts/extract "Student Corpus/Unprocessed Files/" \
             -o "Student Corpus/Plain Files/" -b 5 -m count
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
5. Analyze tagged files. (Script: [analyze](scripts/analyze))
  - output: ___.res.txt
6. Summarize analysis files. (Script: [summarize](scripts/summarize))
  - output: summary.txt

You can see how this all comes together by looking at the [pipeline](scripts/pipeline?ts=4) script. (This script is written in [bash](http://www.gnu.org/software/bash/).)

### Intermediate Files
For each FILE, the following intermediate files may be produced:

* Summer 2015
  + Student Corpus
    * Unprocessed Files
      - FILE.docx
    * Plain Files
      - FILE.raw.txt
    * Processed Files
      - batchXXX
        * FILE.txt
        * FILE.log
        * FILE.memo.txt
    * Tagged Files
      - FILE.tag.txt
      - FILE.memo.tag.txt
    * Results
      - FILE.res.txt
      - FILE.memo.res.txt
    * summary.csv
    * summary.txt
    * summary.memo.txt

The [reset](scripts/reset) script provides a simple way to delete all files generated by the pipeline, but since it can take a long time to tag files, it should only be used when major changes to the plaintext processes occur.

Query Language
--------------

Query Website
-------------

Python uweclang Library - Available Functions
---------------------------------------------

* uweclang
  + batch
    * [batch](uweclang/batch/batch.py)
      - `BATCH_PARSER`
      - `split_ext(filename)`
      - `get_files(search_locations)`
      - `batch_process(process)`
  + binary
    * [docx](uweclang/binary/docx.py)
      - `parse_element_plain(element)`
      - `get_document_xml(filename)`
      - `xml_to_plain(document)`
  + plain
    * [clean](uweclang/plain/clean.py)
      - `punctuation_density(text)`
      - `capitalization_density(text)`
      - `clean_punctuation(text)`
      - `parse_parentheticals(text)`
      - `recombine_parentheticals(parse_tree)`
    * [plain](uweclang/plain/plain.py)
      - `line_split(text)`
  + tagged
    * [tag](uweclang/tagged/tag.py)
      - `tag(text)`
      - `get_tags(tagged)`
      - `read_tagged_string(text)`
      - `tagged_to_plain(tagged)`
      - `parse_tag_parentheticals(tagged)`
      - `recombine_tag_parentheticals(parse_tree)`
      - `ngram(words)`


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
  - [Python 2 Unicode handling](https://pythonhosted.org/kitchen/unicode-frustrations.html)

[nltk.org]: http://www.nltk.org/