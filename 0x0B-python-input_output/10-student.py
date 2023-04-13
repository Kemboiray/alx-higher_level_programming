#!/usr/bin/python3
"""Defines a class, `Student`"""


class Student:
    def __init__(self, first_name: str, last_name: str, age: int):
        """Initialises an instance of `Student`"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary definition of an instance
        Arg:
            attrs (str): optional list of attributes to retrieve.
            If `attrs` is omitted, all attributes are retrieved
        """
        retval = 0
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    retval = self.__dict__
                    break
            if retval == 0:
                retval = {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            retval = self.__dict__
        return retval
