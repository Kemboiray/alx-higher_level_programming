#!/usr/bin/python3
"""Defines `matrix_divided` function"""


def matrix_divided(matrix, div):
    """
    Divides all elements in a matrix
    Args:
        matrix (list): A list of lists of integers or floats
        div (int/float): Number with which to divide the matrix

    Returns: New matrix of quotients, or None if an error is encountered
    """
    e_mat = 'matrix must be a matrix (list of lists) of integers/floats'
    e_len = 'Each row of the matrix must have the same size'
    e_div = 'div must be a number'
    e_zero_div = 'division by zero'
    if (matrix is not None) and (isinstance(matrix, list)):
        for i in matrix:
            if (i is not None) and isinstance(i, list):
                if len(i) != len(matrix[0]):
                    raise TypeError(e_len)
                for j in i:
                    if j is None or not ((isinstance(j, int)
                                         or isinstance(j, float))):
                        raise TypeError(e_mat)
            else:
                raise TypeError(e_mat)
    else:
        raise TypeError(e_mat)
    if div is None or (not (isinstance(div, float) or isinstance(div, int))):
        raise TypeError(e_div)
    if div == 0:
        raise ZeroDivisionError(e_zero_div)

    new_mat = [row[:] for row in matrix]
    for i in range(len(new_mat)):
        for j in range(len(new_mat[i])):
            quotient = new_mat[i][j] / div
            new_mat[i][j] = round(quotient, 2)
    return new_mat
