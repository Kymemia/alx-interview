#!/usr/bin/python3

"""
this is a function that rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    method definition to rotate a matrix
    """
    x = len(matrix)

    for y in range(x):
        for z in range(y, x):
            matrix[y][z], matrix[z][y] = matrix[z][y], matrix[y][z]

    for y in range(x):
        matrix[y].reverse()
