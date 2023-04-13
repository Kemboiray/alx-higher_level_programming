#!/usr/bin/python3
"""Defines a function, `save_to_json_file()`"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using JSON representation
    Args:
        my_obj (object): object
        filename (str): path to file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
