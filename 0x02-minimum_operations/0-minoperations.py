#!/usr/bin/env python3

"""
function to calculate minimum number of operations needed
"""


def minOperations(n):
    """
    method definition
    """
    if n <= 1:
        return 0

    ops = 0
    divider = 2
    while n > 1:
        while n % divider == 0:
            ops += divider
            n //= divider
        divider += 1
    return ops
