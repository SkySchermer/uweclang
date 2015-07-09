UWEC Language Tools
===================

### Table of Contents
* [UWEC Language Tools](#uwec-language-tools)
	* [Table of Contents](#table-of-contents)
	* [Introduction](#introduction)
	* [Pipeline](#pipeline)
	* [Student Corpus Scripts](#student-corpus-scripts)
	* [Available Functions](#available-functions)
	* [Additional Resources](#additional-resources)

### Introduction



Pipeline
--------

* Extract XML from docx files.
* Extract plaintext from XML. (Script: extract.py)
	- output file.raw.txt
* Process plaintext to extract citations, dates, titles, and writer's memos. (Script: scrub.py)
	- output file.txt
	- output file.log
	- output file.memo.txt
* Manually verify each file.
* Tag student files. (Script: tag.py)
	- output file.tag.txt
* Summarize tagged files. (Script: summary.py)

Student Corpus Scripts
----------------------

These scripts can each be used on single files or on entire directories. To process a single file use the following syntax:

	script-name file [output-directory]

If the output directory is not supplied, the resulting output will be in the current directory. To process a directory use the following syntax:

	script-name [-b [batch-size]] input-directory output-directory

If the `-b` flag is provided, the output will be subdivided into batch directories, each containing `batch-size` files. (The default batch size is 10.)


Available Functions
-----------------------------

* `uweclang`
	* `batch`
		* `tools`
	* `binary`
		* `docx`
	* `plain`
		* `student`
		* `tools`
			* ```python
line_split(text, remove_empty_lines=True, strip_lines=True, sep='\n')
			  ```
	* `tagged`


Additional Resources
--------------------