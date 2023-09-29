#!/usr/bin/python3
"Author: TALAINI Mohammed"
import requests
import sys
"""Python script that takes in a URL and an email address
"""
if __name__ == "__main__":
    link = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    resp = requests.post(link, data=payload)
    print(resp.text)
