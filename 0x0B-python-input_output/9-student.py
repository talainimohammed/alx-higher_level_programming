#!/usr/bin/python3
"""No Module"""

class Student:
    """student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict rep of Student
        """
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
