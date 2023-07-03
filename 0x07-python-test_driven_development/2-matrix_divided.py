#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    prevRL = -1
    new_list = []
    for row in matrix:
        if (prevRL != len(row) and prevRL != -1):
            raise TypeError("Each row of the matrix must have the same size")
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
            else:
                new_list.append(round(ele / div, 2))
        prevRL = len(row)

    return new_list
