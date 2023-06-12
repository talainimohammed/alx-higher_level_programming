#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None

    bool_l = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bool_l.append(True)
        else:
            bool_l.append(False)
    return (bool_l)
