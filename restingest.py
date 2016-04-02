#!/usr/bin/env python
#restingest.py

"""
Template answer for REST Workshop
"""
##########################################################################
## Imports
##########################################################################

import json
import pprint
import requests


##########################################################################
## Module Variables/Constants
##########################################################################

DOJ_RELEASES_URL = 'http://www.justice.gov/api/v1/press_releases.json?pagesize=5'

#########################################################################
# Functions
#########################################################################

def fetch_press_releases(URL):
    """
    Performs a GET on the DOJ web service and return the array found in the
    'results' attribute of the JSON response
    """
    # use requests library to execute a GET request and store the results
    response = requests.get(URL)

    # use requests library to decode as json and store the results
    data = response.json()

    # return the 'results' array of press releases
    return data['results']


def main():
    """
    Main execution function to perform required actions
    """
    # fetch array of press releases
    press_releases = fetch_press_releases(DOJ_RELEASES_URL)

    # iterate through press releases
    for release in press_releases:

        # save content to a new file
        # we'll use the unique press release identifier to make the filename
        fname = release['uuid']+'.json'
        content = json.dumps(release)

        with open(fname, 'w') as f:
            f.write(content)


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
