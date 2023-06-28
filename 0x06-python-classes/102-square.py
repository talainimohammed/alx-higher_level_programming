#!/usr/bin/python3

"""No Module"""


class Square:
    """
    class square
    """
    def __init__(self, size=0):
        if self.__validate_size(size):
            self.__size = size

    def __eq__(self, other):
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __validate_size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
