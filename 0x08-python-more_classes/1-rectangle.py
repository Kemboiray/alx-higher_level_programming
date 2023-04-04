#!/usr/bin/python3

"""Definition of class object ``Rectangle``"""


class Rectangle:
    """Class representing a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with width and height attributes.

        Args:
            width (int): the width of the rectangle. Defaults to 0.
            height (int): the height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns private instance attribute ``width``"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private instance attribute ``width``

        Args:
            value (int): the value with which to set ``width``

        Raises:
            TypeError: if ``value`` is a non-integer
            ValueError: if ``value`` is negative
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Returns private instance attribute ``height``"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private instance attribute ``height``

        Args:
            value (int): the value with which to set ``height``

        Raises:
            TypeError: if ``value`` is a non-integer
            ValueError: if ``value`` is negative
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
