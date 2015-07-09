
# UWEC Language Tools

## Pipeline:

* Extract XML from docx files.
* Extract plaintext from XML.
	- output file.raw.txt
* Process plaintext to extract citations, dates, titles, and writer's memos.
	- output file.txt
	- output file.log
	- output file.memo.txt
* Tag student files.
	- output file.tag.txt

## Student corpus scripts:

These scripts can each be used on single files or on entire directories. To process a single file use the following syntax:

	script-name file [output-directory]

If the output directory is not supplied, the resulting output will be in the current directory. To process a directory use the following syntax:

	script-name [-b [batch-size]] input-directory output-directory

If the `-b` flag is provided, the output will be subdivided into batch directories, each containing `batch-size` files. (The default batch size is 10.)



## UWEC Language Tools package:
```
uweclang/
	__init__.py
	batch/
		__init__.py
	binary/
		__init__.py
	plain/
		__init__.py
	tagged/
		__init__.py
```

