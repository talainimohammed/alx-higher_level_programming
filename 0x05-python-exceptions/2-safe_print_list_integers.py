#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    j = 0
    p = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            p += 1
        except (ValueError, TypeError):
            continue
    print()
    return p
