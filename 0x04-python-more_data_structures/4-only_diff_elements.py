#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if isinstance(set_1, set) and isinstance(set_2, set):
        return set(
                list(set_1.difference(set_2)) + list(set_2.difference(set_1)))
