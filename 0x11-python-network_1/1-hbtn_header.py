#!/usr/bin/python3
"Author: TALAINI Mohammed"
import urllib.request
import sys
"""script for testing status of web pages
"""
if __name__ == "__main__":
    link = sys.argv[1]
    with urllib.request.urlopen(link) as resp:
        meta = resp.info()
        for header in meta._headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
