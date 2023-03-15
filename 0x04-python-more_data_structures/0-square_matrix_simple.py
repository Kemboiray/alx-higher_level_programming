#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list) and all(isinstance(row, list) for \
            row in matrix):
        new = matrix.copy()
        for i in range(len(matrix)):
            new[i] = list(map(lambda x: x**2, matrix[i]))

        return new
