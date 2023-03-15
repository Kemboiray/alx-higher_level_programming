#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        new = a_dictionary.copy()
        for key in new:
            new.update({key: new[key] * 2})
        return new
