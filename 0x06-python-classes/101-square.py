#!/usr/bin/python3

"""No Module"""


class Square:
    """
    class square
    """
    def __init__(self, size=0, position=(0, 0)):
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position

    def __str__(self):
        a = 0
        string = ""
        if self.__size == 0:
            string += '\n'
            return
        for a in range(0, self.__position[1]):
            string += '\n'
        a = 0
        for a in range(0, self.__size):
            b = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                string += ' '
            for b in range(0, self.__size):
                string += '#'
            string += '\n'
        return string

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if self.__validate_size(value):
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        a = 0
        if self.__size == 0:
            print()
            return
        for a in range(0, self.__position[1]):
            print()
        a = 0
        for a in range(0, self.__size):
            b = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
            for b in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False

    def __validate_pos(self, position):
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True
