#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        to_print = sorted(a_dictionary)
        for i in to_print:
            print(f'{i}: {a_dictionary[i]}')
