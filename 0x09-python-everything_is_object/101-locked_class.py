#!/usr/bin/python3
"""No Module"""

class LockedClass:
    """Locked class
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
