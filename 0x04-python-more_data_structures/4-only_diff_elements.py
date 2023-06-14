#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set_1 | set_2
    return {i for i in new_set if i in set_1 and i not in set_2 or
            i in set_2 and i not in set_1}
