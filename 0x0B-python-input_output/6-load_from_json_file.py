#!/usr/bin/python3
"""Defines a function, `load_from_json_file()`"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        filename (str): path to file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
