#!/usr/bin/python3
"""No Module"""


def append_write(filename="", text=""):
    """appends onto a utf-8
    """
    with open(filename, 'a', encoding='utf-8') as fl:
        return fl.write(text)
