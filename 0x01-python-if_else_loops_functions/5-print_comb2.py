#!/usr/bin/python3
x = ""
for i in range(0, 100):
    if i < 10:
        x += "0" + str(i) + ", "
    elif i < 99:
        x += str(i) + ", "
    else:
        x += str(i)
print(x)
