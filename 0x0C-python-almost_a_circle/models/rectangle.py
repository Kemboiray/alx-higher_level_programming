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
        if not (type(width) is int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
        if not (type(height) is int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
        if not (type(x) is int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        if not (type(y) is int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def width(self):
        """Retrieves the ``width`` attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the ``width`` attribute"""
        if not (type(value) is int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the ``height`` attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the ``height`` attribute"""
        if not (type(value) is int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieves the ``x`` attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the ``x`` attribute"""
        if not (type(value) is int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieves the ``y`` attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the ``y`` attribute"""
        if not (type(value) is int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height
