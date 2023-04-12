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

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Defines output of `str()` and `print()` for class instance"""
        return f'[Rectangle] {self.__width}/{self.__height}'
