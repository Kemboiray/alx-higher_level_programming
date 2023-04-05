#!/usr/bin/python3
def magic_string():
    if not hasattr(magic_string, 'n'):
        magic_string.n = -1
    magic_string.n += 1
    return "BestSchool" + (", BestSchool")*(magic_string.n)
