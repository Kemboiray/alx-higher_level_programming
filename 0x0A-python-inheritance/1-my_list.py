#!/usr/bin/python3
"""Defines `MyList`, a subclass of `list`"""


class MyList(list):
    """Subclass of `list`"""

    def __init__(self):
        """Initialises class instance"""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list of the elements in the `MyList` object"""
        print(sorted(self))
