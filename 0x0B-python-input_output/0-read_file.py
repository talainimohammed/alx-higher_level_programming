#!/usr/bin/python3
"""No Module"""


def read_file(filename=""):
    """file reading
    """
    with open(filename, encoding='utf-8') as fl:
        print(fl.read(), end='')
