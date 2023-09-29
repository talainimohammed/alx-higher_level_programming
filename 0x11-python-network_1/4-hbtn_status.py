#!/usr/bin/python3
"Author: TALAINI Mohammed"
import requests
"""script for testing status of web pages
"""
if __name__ == "__main__":
    link = "https://intranet.hbtn.io/status"
    resp = requests.get(link)
    content = resp.text
    print_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(print_str)
