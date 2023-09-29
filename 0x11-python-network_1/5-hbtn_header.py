#!/usr/bin/python3
"Author: TALAINI Mohammed"
import requests
import sys
"""Python script that takes in a URL, sends a request to the URL
"""
if __name__ == "__main__":
    link = sys.argv[1]
    resp = requests.get(link)
    meta = resp.headers
    print(meta.get('X-Request-Id'))
