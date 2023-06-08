#!/usr/bin/python3
import hidden_4 as h

if __name__ != "__main__":
    exit()

for n in dir(h):
    if n[0:2] != "__":
        print(n)
