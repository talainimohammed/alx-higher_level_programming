#!/usr/bin/python3
import sys

if __name__ != "__main__":
    str = "{:d} argument"
    nbarg = len(sys.argv) - 1
    if nbarg == 0:
        str += 's.'
    elif nbarg == 1:
        str += ':'
    else:
        str += 's:'
    print(str.format(nbarg))

    i = 0
    for value in sys.argv:
        if i != 0:
            print("{:d}: {:s}".format(i, value))
        i += 1
