#!/usr/bin/python3

# 9-max_integer.py
def max_integer(my_list=[]):
    '''
    Returns the maximum value in a list of integers,
    or `None` if the list is empty
    '''
    if len(my_list) == 0:
        return None
    else:
        return (sorted(my_list))[-1]
