#!/usr/bin/env python3

import os
import re
import sys

import requests

# Functions

def usage(exit_status=0):
    print(f'''Usage: {os.path.basename(sys.argv[0])} [flags]
    -c      CITY    Which city to search
    -s      STATE   Which state to search (Indiana)''')
    sys.exit(exit_status)

def zipcodes(city: str, state: str) -> None:
    url   = f'https://www.zipcodestogo.com/{state}/'
    regex = r'/([^/]+)/[A-Z]{2}/([0-9]{5})/">'  # Review: regex

                                                # Discuss: popen
    #response = os.popen(f'curl -sL {url}').read()
    #for current, zipcode in re.findall(regex, response):

    headers  = {'User-Agent': __name__}         # Discuss: requests
    response = requests.get(url, headers=headers)

                                                # Discuss: re.findall
    for current, zipcode in re.findall(regex, response.text):
        if city is None or city == current:
            print(zipcode)

# Main execution

def main(arguments=sys.argv[1:]):
    state = 'Indiana'
    city  = None                                # Review: None

    while arguments:                            # Review: parsing arguments
        argument = arguments.pop(0)
        if argument == '-c':
            city  = arguments.pop(0)
        elif argument == '-s':
            state = arguments.pop(0)
        elif argument == '-h':
            usage(0)
        else:
            usage(1)

    zipcodes(city, state)

if __name__ == '__main__':
    main()
