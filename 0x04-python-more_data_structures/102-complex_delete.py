#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is not None and type(a_dictionary) is dict:
        items = a_dictionary.items()
        to_d = {key: v for (key, v) in items if value == v}
        for (key, val) in to_d.items():
            del a_dictionary[key]
        return a_dictionary.copy()
