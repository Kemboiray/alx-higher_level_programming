#!/usr/bin/python3
"""Definition of a class object Square"""


class Square:
    """Defines a square with a private instance attribute"""
    def __init__(self, size=0):
        """Initialises instance attribute

        Args:
            size (int): value with which to initialise attribute

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size)**2
