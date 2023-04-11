#!/usr/bin/python3
"""Defines function `is_same_class`"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class
    Args:
        obj: object
        a_class: specified class

    Returns: True or False.
    """
    return type(obj) == a_class
