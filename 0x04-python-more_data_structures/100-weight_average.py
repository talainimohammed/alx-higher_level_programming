#!/usr/bin/python3

def weight_average(my_list=[]):
    i = len(my_list)
    if i == 0:
        return 0
    scores = [score*weight for (score, weight) in my_list]
    return sum(scores) / sum([weight for (score, weight) in my_list])
