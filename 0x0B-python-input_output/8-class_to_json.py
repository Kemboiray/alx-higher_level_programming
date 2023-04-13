#!/usr/bin/python3
"""Defines `class_to_json()`"""


def class_to_json(obj):
    """Returns the dictionary description of a class object, `obj`"""
    return obj.__dict__
