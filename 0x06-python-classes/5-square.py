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

    def area(self):
        """Returns the current square area"""
        return (self.__size)**2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
