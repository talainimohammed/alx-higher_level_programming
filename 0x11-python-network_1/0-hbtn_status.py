#!/usr/bin/python3
"Author: TALAINI Mohammed"
import urllib.request
"""script for testing status of web pages
"""
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as resp:
        bytes_content = resp.read()
        content = bytes_content.decode('utf-8')
        print_rsp = '''Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}'''.format(type(bytes_content), bytes_content, content)
        print(print_rsp)
