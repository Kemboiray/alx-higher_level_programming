#!/usr/bin/python3
"""Defines ``add_integer()``"""


def add_integer(a, b=98):
    """Adds two real numbers
    Args:
        a (int or float): number
        b (int or float): second number
    Returns:
        Integer result of the addition
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    result = int(a) + int(b)
    return result
