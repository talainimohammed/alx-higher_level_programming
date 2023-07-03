#!/usr/bin/python3

def print_square(size):
    """
    prints a square of given size
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    s = int(size)
    i = 0

    for i in range(0, s):
        j = 0
        for j in range(0, s):
            print('#', end='')
        print()
