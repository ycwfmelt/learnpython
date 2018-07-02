'''
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<{0}>'.format(tag))

    def handle_endtag(self, tag):
        print('</{0}>'.format(tag))

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s:' % name)

    def handle_charref(self, name):
        print('&#%s:' % name)

parser = MyHTMLParser()
parser.feed()

'''

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re


class MyHTMLParser(HTMLParser):
    a_t1 = False
    a_t2 = False
    a_t3 = False

    def __init__(self):
        HTMLParser.__init__(self)
        self.information = []
        self.information_all = {}
