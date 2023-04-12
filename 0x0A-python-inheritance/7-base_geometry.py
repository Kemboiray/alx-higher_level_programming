#!/usr/bin/python3
"""Defines an empty class `BaseGeometry`"""


class BaseGeometry:
    """Class pending implementation of method, `area`"""
    def area(self):
        """Raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates `value` is an integer and positive
        Args:
            name (str): name associated with `value`
            value (int): object to validate
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
