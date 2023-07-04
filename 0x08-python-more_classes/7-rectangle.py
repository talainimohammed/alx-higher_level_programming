#!/usr/bin/python3
"""NO Module"""


class Rectangle():
    """rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiation method creation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ provides __str__ method
        """
        if self.width == 0 or self.height == 0:
            return ""

        s = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                s += str(self.print_symbol)
            if i != self.height - 1:
                s += '\n'
        return s

    def __repr__(self):
        """ provides __repr__ method
        """
        s = "Rectangle("
        s += str(self.width)
        s += ", " + str(self.height) + ")"
        return s

    def __del__(self):
        """ called when a rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ gets the area of rectangle """
        return (self.width * self.height)

    def perimeter(self):
        """ gets the perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))
