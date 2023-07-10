#!/usr/bin/python3
"""No Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle shape
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """custom str method for str
        """
        str = "[Rectangle] "
        str += str(self.__width) + '/' + str(self.__height)
        return str

    def area(self):
        """overrides parent's method for area
        """
        return (self.__width * self.__height)
