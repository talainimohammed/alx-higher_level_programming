#!/usr/bin/python3
"""No Module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square shape class
    """
    def __init__(self, size):
        """instantiation method
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """overide magic str
        """
        str = "[Square] " + str(self.__size) + '/'
        str += str(self.__size)
        return str
