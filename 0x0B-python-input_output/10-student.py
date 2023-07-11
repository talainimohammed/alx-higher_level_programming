#!/usr/bin/python3
"""No Module"""


class Student:
    """student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict rep of Student
        """
        is_all_str = True
        if isinstance(attrs, list):
            for el in attrs:
                if not isinstance(el, str):
                    is_all_str = False
        else:
            is_all_str = False

        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys()) and
                (not is_all_str or key in attrs)}
