#!/usr/bin/python3
"Author: TALAINI Mohammed"
import urllib.request
import urllib.parse
import sys
"""Python script that takes in a URL and an email
"""
if __name__ == "__main__":
    link = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    payload = urllib.parse.urlencode(payload)
    payload = payload.encode('ascii')
    req = urllib.request.Request(link, payload)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
