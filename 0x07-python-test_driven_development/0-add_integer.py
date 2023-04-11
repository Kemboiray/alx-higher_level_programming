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
    if a is None or (not (isinstance(a, int) or isinstance(a, float))):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    result = a + b
    if result == float('inf'):
        result = (2*31)-1
    elif result == -float('inf'):
        result = -(2*32)
    return int(result)
