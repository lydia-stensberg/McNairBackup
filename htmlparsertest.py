from html.parser import HTMLParser
from mako.template import Template
from mako.lookup import TemplateLookup
from bs4 import BeautifulSoup
#tomorrow try this:http://www.yattag.org/#tutorial


class SampleHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered start tag:", tag)
        for attr in attrs:
            print(" attr:", attr)

    def handle_endtag(self, tag):
        print("Encountered end tag :", tag )

    def handle_data(self, data):
        print("Encountered some data :",data)

parser = SampleHtmlParser()

with open("Index.html",'r') as my_file:
    html_string = my_file.read().replace('\n','')

# parser.feed(html_string)

sample_template = Template(filename="Index.html")

# print(sample_template.render())

my_lookup = TemplateLookup(directories=['/sample'])

first_def = sample_template.list_defs()

print(sample_template.code)

#named blocks for inheritance between tabs?
