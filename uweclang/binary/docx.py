"""UWEC Language Tools docx module

    Provides functions for handling Microsoft Word docx files.
"""
# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

# Standard imports
import sys
import os
import zipfile
import re

from xml.etree.cElementTree import XML


def parse_element_plain(element):
    """Recursively parses an ElementTree Element object and returns a string
    containing the text of each tag.

    Arguments:
        element (Element): The root element.

    Returns:
        (str): The text under the root.
    """
    text = []

    if element.text is not None:
        text.append(element.text)

    if element.tag.endswith('}br') or element.tag.endswith('}p'):
        text.append('\n')

    for child in element:
        text.extend(parse_element_plain(child))

    return text



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
    root = XML(document.encode('utf-8'))

    return ''.join(parse_element_plain(root))

