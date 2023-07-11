#!/usr/bin/python3
"""No Module"""


def append_after(filename="", search_string="", new_string=""):
    """appends after search string
    """
    with open(filename, 'r', encoding='utf-8') as fl:
        ln = fl.readlines()

    for i, line in enumerate(ln):
        if search_string in line:
            ln.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as fl:
        content = "".join(ln)
        fl.write(content)
