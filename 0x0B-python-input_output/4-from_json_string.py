#!/usr/bin/python3
"""module for deserializing json
"""


import json


def from_json_string(my_str):
    """deserializes a JSON string back to a python object
    """
    return json.loads(my_str)
