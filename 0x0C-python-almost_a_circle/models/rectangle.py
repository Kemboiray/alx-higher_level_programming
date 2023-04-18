#!/usr/bin/python3
"""Defines class ``Rectangle``"""
from models.base import Base


class Rectangle(Base):
    """Defines a ``Rectangle`` object``"""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Class constructor
        Args:
            width: initial value of ``__width``
            height: initial value of ``__height``
            x, y: coordinates
        """
        super().__init__(id)
        if not (type(width) is int or type(width) is float):
            raise TypeError('width must be a real number')
        elif width < 0:
            raise ValueError('width must be positive')
        else:
            self.__width = width
        if not (type(height) is int or type(height) is float):
            raise TypeError('height must be a real number')
        elif height < 0:
            raise ValueError('height must be positive')
        else:
            self.__height = height
        if not (type(x) is int or type(x) is float):
            raise TypeError('x must be a real number')
        else:
            self.__x = x
        if not (type(y) is int or type(y) is float):
            raise TypeError('y must be a real number')
        else:
            self.__y = y

    @property
    def width(self):
        """Retrieves the ``width`` attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the ``value`` attribute"""
        if not (type(value) is int or type(value) is float):
            raise TypeError('value must be a real number')
        elif value < 0:
            raise ValueError('value must be positive')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the ``height`` attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the ``value`` attribute"""
        if not (type(value) is int or type(value) is float):
            raise TypeError('value must be a real number')
        elif value < 0:
            raise ValueError('value must be positive')
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieves the ``x`` attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the ``x`` attribute"""
        if not (type(x) is int or type(x) is float):
            raise TypeError('x must be a real number')
        else:
            self.__x = x

    @property
    def y(self):
        """Retrieves the ``y`` attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the ``y`` attribute"""
        if not (type(y) is int or type(y) is float):
            raise TypeError('y must be a real number')
        else:
            self.__y = y
