#!/usr/bin/python3
"""No Module"""


class BaseGeometry():
    """for use with shapes
    """

    def area(self):
        """instance method to calculate area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer input
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
