#!/usr/bin/python3
def uppercase(str):
    y = ""
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
            y += chr(ord(x) - 32)
        else:
            y += "{}".format(x)
    print(y)
