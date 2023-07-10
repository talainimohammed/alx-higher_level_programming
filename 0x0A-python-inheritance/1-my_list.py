#!/usr/bin/python3
"""No Module"""


class MyList(list):
    """extended version
    """
    def print_sorted(self):
        """prints the list
        """
        cp = self[:]
        cp.sort()
        print(cp)
