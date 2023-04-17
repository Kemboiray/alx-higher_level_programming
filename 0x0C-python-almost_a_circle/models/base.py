#!/usr/bin/python3
"""Defines the first class ``Base``"""


class Base:
    """Base class for this project"""
    __nb_objects = 0

    def __init__(self, id: int = None):
        """Class constructor
        Arg:
            id: unspecified
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
