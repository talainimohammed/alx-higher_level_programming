#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

nbarg = len(argv) - 1
if nbarg != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] == '+':
    f = add
elif argv[2] == '-':
    f = sub
elif argv[2] == '*':
    f = mul
elif argv[2] == '/':
    f = div
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)

res = f(int(argv[1]), int(argv[3]))
print("{:d} {:s} {:d} = {:d}".format(int(argv[1]),
    argv[2], int(argv[3]), res))
