#!/usr/bin/python3

# 10-divisible_by_2.py
def divisible_by_2(my_list=[]):
    '''
    Finds all multiples of 2 in a list
    Args:
        my_list: list
    Return:
        Truth list with corresponding elements `True` or `False`
    '''
    new_list = my_list.copy()
    for i in range(0, len(my_list)):
        new_list[i] = (my_list[i] % 2 == 0)
    return new_list
