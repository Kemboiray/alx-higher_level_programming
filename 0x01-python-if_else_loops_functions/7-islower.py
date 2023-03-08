#!/usr/bin/python3


def islower(c):  # checks for lowercase character
    '''Returns True if a lowercase character is passed and False otherwise'''
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
