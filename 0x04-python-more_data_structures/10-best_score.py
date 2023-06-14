#!/usr/bin/python3

def best_score(a_dictionary):
    win_num = 0
    win = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > win_num:
                win_num = value
                win = key
    return win
