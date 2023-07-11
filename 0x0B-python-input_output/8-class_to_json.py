#!/usr/bin/python3
"""No module"""


def class_to_json(obj):
    """creates a json representation
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
