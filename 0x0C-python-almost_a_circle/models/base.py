#!/usr/bin/python3
"""Defines the first class ``Base``"""
import json


class Base:
    """Base class for this project"""
    __nb_objects = 0

    def __init__(self, id: int = None):
        """Class constructor
        Arg:
            id: unspecified
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return json string representation of a list of dictionaries
        Arg:
            list_dictionaries: a list of dictionaries
        """
        if not (isinstance(list_dictionaries, list)
                or list_dictionaries is None):
            raise TypeError(f'Expected a list, or None, \
got {type(list_dictionaries)}')
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        for item in list_dictionaries:
            if not isinstance(item, dict):
                raise TypeError(f'Expected a dict, got {type(item)}')
        return json.dumps(list_dictionaries)
