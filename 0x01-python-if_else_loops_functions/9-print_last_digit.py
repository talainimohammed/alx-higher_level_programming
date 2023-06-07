#!/usr/bin/python3
def print_last_digit(number):
    nb = int(repr(number)[-1])
    print(nb, end='')
    return nb
