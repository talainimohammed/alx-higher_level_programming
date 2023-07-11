#!/usr/bin/python3
"""No Module"""


def pascal_triangle(n):
    """gets pascal triangle for n
    """
    ret = []
    for i in range(0, n):
        mat_l = len(ret)
        if mat_l <= 1:
            ret.append([1 for q in range(0, mat_l + 1)])
        else:
            new_r = []
            for j in range(0, len(ret[i - 1]) + 1):
                if j == 0 or j == len(ret[i - 1]):
                    new_r.append(1)
                else:
                    new_r.append(ret[i - 1][j - 1] + ret[i - 1][j])
            ret.append(new_r)
    return ret
