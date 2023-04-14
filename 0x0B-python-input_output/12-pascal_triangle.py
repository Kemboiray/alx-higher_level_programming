#!/usr/bin/python3
"""Function definitions"""


def pascal_triangle(n: int):
    """Returns the pascal's triangle for a given exponent, `n`"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [[1], [1, 1]]
    while True:
        if len(triangle) >= n:
            break
        t = []
        temp = triangle[-1]
        for i in range(len(temp) - 1):
            t.append(temp[i] + temp[i+1])
        t.insert(0, 1)
        t.append(1)
        triangle.append(t[:])
    return triangle
