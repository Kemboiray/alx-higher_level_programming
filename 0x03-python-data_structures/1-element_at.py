#!/usr/bin/python3

# 1-element_at.py
def element_at(my_list, idx):
    '''
    Returns element at a given index, `idx` in a list, `my_list`
    If `idx` is negative or out of bounds, returns `None`
    '''
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
