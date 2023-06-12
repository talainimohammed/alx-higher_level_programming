#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    l_len = len(my_list)
    if l_len <= idx or idx < 0:
        return (my_list)
    my_list[idx] = element
    return (my_list)
