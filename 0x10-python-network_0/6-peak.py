#!/usr/bin/python3
"""Defines the function `find_peak`"""


def find_peak(list_of_integers=[]):
    """Return a peak in an unsorted list of integers"""

    ints = list_of_integers
    if not ints:
        return None
    if ints[0] > ints[1]:
        return ints[0]
    if ints[-1] > ints[-2]:
        return ints[-1]
    for i in range(1, len(ints) - 1):
        if ints[i - 1] < ints[i] and ints[i + 1] < ints[i]:
            return ints[i]
    return ints[-1]
