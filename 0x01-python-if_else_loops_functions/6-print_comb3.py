#!/usr/bin/python3
x = ""
for i in range(0, 9):
    for j in range(1, 10):
        if j > i:
            x += "{0:d}".format(i) + "{0:d}".format(j)
            if i != 8 or j != 9:
                x += ", "
print(x)
