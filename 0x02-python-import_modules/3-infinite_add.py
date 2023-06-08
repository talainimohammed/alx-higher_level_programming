#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

i = 0
res = 0
for argvalue in sys.argv:
    if i != 0:
        res += int(argvalue)
    else:
        i += 1
print("{:d}".format(res))
