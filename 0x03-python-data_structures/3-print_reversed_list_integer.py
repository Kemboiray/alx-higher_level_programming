#!/usr/bin/python3

# 3-print_reversed_list_integer.py
def print_reversed_list_integer(my_list=[]):
    '''
    prints all integers of a list, in reverse order
    '''
    if not (isinstance(my_list, list)):
        return
    my_list.reverse()
    for i in my_list:
        print('{:d}'.format(i))
