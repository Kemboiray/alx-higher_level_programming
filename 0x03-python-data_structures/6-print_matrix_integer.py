#!/usr/bin/python3

# 6-print_matrix_integer.py
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j == i[-1]:
                print('{:d}'.format(j), end='')
            else:
                print('{:d}'.format(j), end=', ')
        print()
