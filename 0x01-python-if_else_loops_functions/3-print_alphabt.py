#!/usr/bin/python3
x = ""
for i in range(97, 123):
    if i != 101 and i != 113:
        x += "{0:c}".format(i)
print(x, end = ' ')
