#!/usr/bin/python3
"""Definition of a class object Square"""


class Square:
    """Defines a square with a private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialises instance attribute

        Args:
            size (int): value with which to initialise attribute
            position (tuple): tuple defining position

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if not (isinstance(position, tuple) and len(position) == 2
                and isinstance(position[0], int)
                and isinstance(position[1], int) and position[0] >= 0
                and position[1] >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    @property
    def size(self):
        """Retrieves the attribute ``size``"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the attribute ``size``"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves ``position``"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the attribute ``position``"""
        if not (isinstance(value, tuple) and len(value) == 2
                and isinstance(value[0], int)
                and isinstance(value[1], int) and value[0] >= 0
                and value[1] >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size)**2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        s, p = self.__size, self.__position
        if s == 0:
            print()
            return
        for y in range(p[1]):
            print()
        for i in range(s):
            for x in range(p[0]):
                print(' ', end='')
            for j in range(s):
                print('#', end='')
            print()
