#!/usr/bin/python3
"""Defines a function, `append_write()`"""


def append_write(filename='', text=''):
    """
    Appends into a text file (UTF8)
    Args:
        filename (str): file path
        text (str): text to append

    Returns: number of characters appended
    """
    with open(str(filename), 'a', encoding='utf-8') as f:
        n = f.write(str(text))
    return n
