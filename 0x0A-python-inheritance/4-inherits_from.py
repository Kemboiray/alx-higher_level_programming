#!/usr/bin/python3
"""Defines function `inherits_from`"""


def inherits_from(obj, a_class):
    """
    Checks if an object is a child or descendant of a class
    Args:
        obj: object
        a_class: specified class

    Returns: True or False.
    """
    value = isinstance(obj, a_class) and (type(obj) != a_class)
    return value
