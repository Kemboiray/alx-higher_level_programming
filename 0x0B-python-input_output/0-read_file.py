#!/usr/bin/python3
"""Defines a function, `read_fike()`"""


def read_file(filename=''):
    """
    Reads a text file (UTF8) and prints it to stdout
    Arg:
        filename (str): file path
    """
    with open(str(filename)) as f:
        print(f.read(), end='')
