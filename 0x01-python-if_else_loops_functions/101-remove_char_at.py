#!/usr/bin/python3
def remove_char_at(str, n):
    x = ''
    if n < 0:
        return str
    for i in range(len(str)):
        if i != n:
            x += "{}".format(str[i])
    return x
