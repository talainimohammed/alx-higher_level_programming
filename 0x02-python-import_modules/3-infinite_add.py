#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

i = 0
result = 0
for argvalue in sys.argv:
    if i != 0:
        result += int(argvalue)
    else:
        i += 1
print("{:d}".format(result))
