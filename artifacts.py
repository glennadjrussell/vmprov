import os
import urllib2
from bs4 import BeautifulSoup, SoupStrainer

BUILD_HTTP_URL = os.environ["BUILD_SERVER"]

def get_latest_build(match):
   page = urllib2.urlopen(BUILD_HTTP_URL)

   for link in BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer('a')):
      if link.has_attr('href'):
         print link['href']

if __name__ == '__main__':
   get_latest_build('staxx')

