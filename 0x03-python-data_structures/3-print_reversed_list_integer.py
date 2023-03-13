#!/usr/bin/python3

# 3-print_reversed_list_integer.py
def print_reversed_list_integer(my_list=[]):
    '''
    prints all integers of a list, in reverse order
    '''
    i = len(my_list) - 1
    while i >= 0:
        elem = my_list[i]
        print('{:d}'.format(elem))
        i -= 1
