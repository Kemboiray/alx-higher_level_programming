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

    @classmethod
    def save_to_file(cls, list_objs: list):
        """Write the JSON string representation of ``list_objs`` to a file
        Arg:
            list_objs: List of instances inheriting from ``Base``
        """
        filename = f'{cls.__name__}.json'
        dict_list = None
        if isinstance(list_objs, list) and len(list_objs):
            for item in list_objs:
                if not (isinstance(item, Base)):
                    e = f'Expected a `Base` instance, got {type(item)}'
                    raise TypeError(e)
            dict_list = [cls.to_dictionary(obj) for obj in list_objs]
        to_write = cls.to_json_string(dict_list)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(to_write)

    @classmethod
    def create(cls, **dictionary):
        """Return a subclass instance with attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
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

    @staticmethod
    def from_json_string(json_string: str):
        """Return the list of the JSON string representation ``json_string``
        """
        if json_string is None or (isinstance(json_string, str)
                                   and len(json_string) == 0):
            return []
        if not isinstance(json_string, str):
            raise TypeError(f'Expected a `str`, got {type(json_string)}')
        return json.loads(json_string)
