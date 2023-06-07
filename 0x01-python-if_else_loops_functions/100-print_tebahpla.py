#!/usr/bin/python3
x = ""
for i in reversed(range(97, 123)):
    if i % 2 != 0:
        i = i - 32
    x += "{0:c}".format(i)
print(x, end='')
