#!/usr/bin/python3
"""
function that returns a list of lists
of integers represnting the Pascal's triangle of n.

Returns an empty list if n <= 0
"""


def pascal_triangle(n):
    """method definition"""
    if n < 0:
        return []

    triangle = [[1]]
    for x in range(1, n):
        row = [1]
        for j in range(1, x):
            row.append(triangle[x-1][j-1] + triangle[x-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
