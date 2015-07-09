

Pipeline:
	Extract XML from docx files.
	Extract plaintext from XML.
		- output file.raw.txt
	Process plaintext to extract citations, dates, titles, and writer's memos.
		- output file.txt
		- output file.log
		- output file.memo.txt
	Tag student files.
		- output file.tag.txt


uweclang/
	__init__.py

	text/
		TaggedText
		capitalization_density
		punctuation_density
		tag_density
		tag
	tools/
		docx_to_plain
		scrub_student_corpus

