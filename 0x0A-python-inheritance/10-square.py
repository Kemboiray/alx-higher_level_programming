#!/usr/bin/python3
"""Defines `Square`, a subclass of `('9-rectangle').Rectangle`"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """
        Initialises class instance
        Arg:
            size (int): length dimension of object
        """
        self.integer_validator('size', size)
        self._Rectangle__width = size
        self._Rectangle__height = size
