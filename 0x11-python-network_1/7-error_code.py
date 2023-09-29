#!/usr/bin/python3
"Author: TALAINI Mohammed"
import requests
import sys
"""Python script that takes in a URL, sends a request to the URL
"""
if __name__ == "__main__":
    link = sys.argv[1]
    resp = requests.get(link)
    if resp.status_code != requests.codes.ok:
        print('Error code: {}'.format(resp.status_code))
    else:
        print(resp.text)
