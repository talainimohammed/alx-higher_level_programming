#!/usr/bin/python3
x = ""
for i in range(0, 100):
    if i < 10:
        x += "0" + "{0:d}".format(i) + ", "
    elif i < 99:
        x += "{0:d}".format(i) + ", "
    else:
        x += "{0:d}".format(i)
print(x)
