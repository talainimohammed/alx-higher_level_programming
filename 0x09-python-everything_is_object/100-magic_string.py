#!/usr/bin/python3
def magic_string():
    from counter import Count
    Count.i += 1
    return ", ".join(["BestSchool" for i in range(0, Count.i)])
