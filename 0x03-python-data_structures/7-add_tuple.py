#!/usr/bin/python3

# 7-add_tuple.py
def add_tuple(tuple_a=(), tuple_b=()):
    '''
    Adds corresponding elements of two tuples, `tuple_a` and `tuple_b`

    Return: a tuple of the sums
    '''
    a = (0, 0)
    tuple_a += a
    tuple_b += a
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    return (x, y)
