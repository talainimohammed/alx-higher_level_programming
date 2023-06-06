#!/usr/bin/python3
def print_last_digit(number):
    if type(number) == int:
        nb = int(repr(number)[-1])
        return nb
    else:
        return "TypeError"
