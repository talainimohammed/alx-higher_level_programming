#!/usr/bin/python3
"""module for use
"""


import json


def save_to_json_file(my_obj, filename):
    """saves obj to a file, overwriting previous contents
    """
    with open(filename, 'w', encoding='utf-8') as fl:
        return fl.write(json.dumps(my_obj))
