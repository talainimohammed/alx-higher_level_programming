#!/usr/bin/python3
"""module for loading data
"""


import json


def load_from_json_file(filename):
    """loads an object from json file containing json
    """
    with open(filename, encoding='utf-8') as fl:
        return (json.loads(fl.read()))
