#!/usr/bin/python3

def text_indentation(text):
    """
    prints a string of text with 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = ""
    specials = ['.', '?', ':']
    for c in text:
        s += c
        if c in specials:
            s += "\n\n"
    print(s, end='')
