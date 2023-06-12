#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return (my_list)
    new_l = my_list[0:]
    new_l[idx] = element
    return (new_l)
