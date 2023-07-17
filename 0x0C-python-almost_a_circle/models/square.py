#!/usr/bin/python3
"""module for square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class for use as an object
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        build = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
        return build

    def update(self, *args, **kwargs):
        """takes an *args argument and sets arguments respective
            to instantiation function
        """
        if args is not None and len(args) > 0:
            for j, arg in enumerate(args):
                if j == 0:
                    self.id = arg
                elif j == 1:
                    self.size = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """gets the dictionary
        """
        new_dict = super().to_dictionary()
        del new_dict['height']
        del new_dict['width']
        new_dict['size'] = self.size
        return new_dict

    def to_csv(self):
        """returns a list containing csv
        """
        return [self.id, self.size, self.x, self.y]

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
