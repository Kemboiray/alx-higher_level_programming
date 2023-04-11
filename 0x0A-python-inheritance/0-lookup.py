#!/usr/bin/python3
"""Defines function `lookup`"""


def lookup(obj):
    """
    Returns the list of available attributes and methods in an object
    Args:
        obj (object): object
    """
    return list(dir(obj))
