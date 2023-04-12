#!/usr/bin/python3
"""Defines a function, `write_file()`"""


def write_file(filename='', text=''):
    """
    Writes into a text file (UTF8)
    Args:
        filename (str): file path
        text (str): text to write

    Returns: number of characters written
    """
    with open(str(filename), 'w', encoding='utf-8') as f:
        n = f.write(str(text))
    return n
