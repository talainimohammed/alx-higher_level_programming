#!/usr/bin/python3
"""No Module"""


def copy_list(l):
    """copy of a list
    """
    if not isinstance(l, list):
        return None
    return l[:]
