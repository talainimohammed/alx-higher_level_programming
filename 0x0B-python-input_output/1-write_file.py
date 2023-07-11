#!/usr/bin/python3
"""No Module"""


def write_file(filename="", text=""):
    """writes to a utf-8
    """
    with open(filename, 'w', encoding='utf-8') as fl:
        return fl.write(text)
