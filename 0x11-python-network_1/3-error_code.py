#!/usr/bin/python3
"Author: TALAINI Mohammed"
import urllib.request
import urllib.error
import sys
"""script for testing status of web pages
"""
if __name__ == "__main__":
    link = sys.argv[1]
    try:
        with urllib.request.urlopen(link) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
