#!/usr/bin/python3


def islower(c):  # checks for lowercase character
    '''Returns True if a lowercase character is passed and False otherwise'''
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False


def uppercase(str):  # prints given string in uppercase
    '''Appends newline to `str` and manipulates new string using built-ins'''
    temp = str + '\n'
    for c in temp:
        if islower(c):
            print('{}'.format(chr(ord(c) - 32)), end='')
        else:
            print('{}'.format(c), end='')
