#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    i = key
    if i is not "" and i in a_dictionary:
        a_dictionary.pop(i)
    return (a_dictionary.copy())
