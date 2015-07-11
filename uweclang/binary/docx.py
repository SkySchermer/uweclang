"""UWEC Language Tools docx module

    Provides functions for handling Microsoft Word docx files.
"""

import sys
import os
import zipfile
import re
import xml.etree.ElementTree


def get_document_xml(filename,
                     encoding='utf-8',
                     doc_part='word/document.xml',
                     verbosity=1):
    """Opens a Microsoft Word docx file and returns the raw XML data for the
    document's text content.

    Arguments:
        filename (str): The name of the docx file to open.
        encoding (Optional[str]): The file encoding. Defaults to 'utf-8'.
        doc_part (Optional[str]): The XML document to open. Defaults to
            'word/document.xml'.
        verbosity (int): The verbosity of the output.

    Returns:
        The document's XML data as a string.
    """
    if verbosity >= 2:
        print('Unzipping file', os.path.basename(filename))

    with zipfile.ZipFile(filename) as document:

        # Open document XML from the docx (ZIP) file.
        doc_file = document.open(doc_part, "r")

        if verbosity >= 3:
            print('Reading file output')

        data = doc_file.read()

        if verbosity >= 3:
            print('Decoding data using', doc_part)

        return data.decode(encoding)


def xml_to_plain(document, verbosity=1):
    """Extracts plaintext from Word XML document data.

    Arguments:
        document (str): The xml document to parse.
        verbosity (int): The verbosity of the output.

    Returns:
        The document in plaintext.
    """
    # This is a list of find/replace pairs for editing the docx XML data. See
    #   https://docs.python.org/2/library/re.html
    # for details.
    edits = [{'FIND': '</w:p>', 'REPLACE': '\n'},  # Preserve paragraphs.
             {'FIND': '<[^>]+>', 'REPLACE': ''},  # Remove formatting XML.
             {'FIND': '[\x7f\x80]+', 'REPLACE': ''}] # Remove non-printable
                                                     # characters.

    # Perform text substitutions on XML data:
    for edit in edits:
        if verbosity >= 3:
            print('Performing edit "{}" -> "{}"'.format(edit['FIND'],
                                                        edit['REPLACE']))

        document = re.sub(edit['FIND'], edit['REPLACE'], document)

    return document
