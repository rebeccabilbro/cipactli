#!/usr/bin/env python
# rssingest.py

"""
Sample solution for RSS exercise
"""
##########################################################################
## Imports
##########################################################################

import re

import requests
import feedparser


##########################################################################
## Module Variables/Constants
##########################################################################

RSS_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'


##########################################################################
## Functions
##########################################################################

def slugify(value):
    """
    Converts to ASCII. Converts spaces to hyphens. Removes characters that
    aren't alphanumerics, underscores, or hyphens. Converts to lowercase.
    Also strips leading and trailing whitespace.
    Note: This is not production code
    """
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)


def save_article(title, content):
    """
    Save HTML content using a slugged version of the title as the basis for
    the filename
    """
    fname = slugify(title)+'.html'
    with open(fname, 'w') as f:
        f.write(content.encode('utf-8'))


def main():
    """
    Main execution
    """
    # grab RSS data and parse it
    feed = feedparser.parse(RSS_URL)

    # loop through each article/RSS item
    # remember that the .parse method in feedparser provides a list of items feed.entries
    # in the same order as the original feed. so the first item is available in feed.entries[0]
    for entry in feed.entries:

        # fetch article using url
        url = entry['id']
        title = entry['title']
        content = requests.get(url)

        # save to disk or print an error message
        try:
            save_article(title, content.text)
        except:
            print "Sorry, couldn't get the content for %s" %title


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
