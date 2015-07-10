#! /usr/bin/env python

import sys
import re
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    visited_pages = []
    pages_to_visit = []
    terms = []

    current_url = None
    attrs = None
    dtype = None
    collect = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.collect = True
            self.dtype = 'LINK'
            self.attrs = attrs
        elif tag == 'td' and ('class', 'id-term') in attrs:
            self.collect = True
            self.dtype = 'TERM'
        else:
            self.collect = False
            self.dtype = None

    def handle_data(self, data):
        if self.collect:
            data = data.strip()
            if self.dtype == 'LINK' and re.fullmatch('[A-Z]\d?|X-Y-Z', data):
                # print('found link:', data)
                for attr in self.attrs:
                    if attr[0] == 'href':
                        self.pages_to_visit.append(urljoin(self.current_url, attr[1]))

            elif self.dtype == 'TERM':
                self.terms.append(data)

            self.collect = False

    def get_terms(self):
        return self.terms


    def start(self, url):

        if url not in self.visited_pages:
            self.current_url = url
            print('Scanning page:', url)
            page = urllib.request.urlopen(url).read()
            self.visited_pages.append(url)
            self.feed(re.sub('<br/>', ' ', page.decode("utf-8")))

        while self.pages_to_visit:
            next_url = self.pages_to_visit.pop()

            if next_url not in self.visited_pages:
                self.current_url = next_url
                print('Scanning page:', next_url)
                page = urllib.request.urlopen(next_url).read()
                self.visited_pages.append(next_url)
                self.feed(re.sub('<br/>|<em>|</em>', ' ', page.decode("utf-8")))


if __name__ == '__main__':
    url = 'http://www.learn-english-today.com/idioms/idiom-alphalists/alpha-list_A/id_A4-allsizzle-apple.html'

    parser = MyHTMLParser()
    parser.start(url)

    res = open('terms.txt', 'w')
    for term in parser.get_terms():
        print(term.strip(), file=res)





