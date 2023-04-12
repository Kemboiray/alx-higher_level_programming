#!/usr/bin/python3
"""Defines `Rectangle`, a subclass of `BaseGeometry`"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Child class of BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialises `Rectangle` instance
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
