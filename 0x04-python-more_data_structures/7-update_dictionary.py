#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if isinstance(a_dictionary, dict):
        a_dictionary.update({key: value})
        return a_dictionary
