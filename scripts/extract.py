#! /usr/bin/env python

import sys
import argparse
import uweclang

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Extracts plaintext from docx files',
        parents=[uweclang.BATCH_PARSER])


    parser.add_argument('-e', '--extensions',
                        nargs='*',
                        default='.docx',
                        metavar='ext',
                        dest='ext',
                        help='accepted file extensions for input')

    print(parser.parse_args())
