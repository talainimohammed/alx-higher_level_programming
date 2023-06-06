#!/usr/bin/python3
def uppercase(str):
    y = ""
    for x in str:
        i = 97
        j = 65
        while i < 123:
            while j < 91:
                if ord(x) == i:
                    y += "{0:c}".format(j)
                j += 1
                i += 1   
    print(y)
