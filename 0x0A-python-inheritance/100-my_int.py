#!/usr/bin/python3
"""No Module"""


class MyInt(int):
    """inversed int, overriding operator methods
    """

    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
