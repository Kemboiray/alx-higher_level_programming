#!/usr/bin/python3

# 11-delete_at.py
def delete_at(my_list=[], idx=0):
    '''
    deletes the item at a specific position in a list
    Args:
        `my_list`: list
        `idx`: position
    Return:
        modified list if valid index was given, original list otherwise
    '''
    if idx >= 0 and idx < len(my_list):
        my_list[idx:idx+1] = []
    return my_list
