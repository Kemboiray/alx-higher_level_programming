#!/usr/bin/python3

# 3-print_reversed_list_integer.py
def print_reversed_list_integer(my_list=[]):
    '''
    prints all integers of a list, in reverse order
    '''
    new_list = sorted(my_list, reverse=True)
    for i in new_list:
        print('{:d}'.format(i))
