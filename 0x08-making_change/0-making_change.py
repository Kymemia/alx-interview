#!/usr/bin/python3
"""
function that returns the fewest number of coins needed
to meet a given amount, total
Solves the coin change problem using dynamic programming
"""


def makeChange(coins, total):
    """
    function that solves the coin change problem
    """
    if total <= 0:
        return 0

    r = [float("infinity")] * (total + 1)
    r[0] = 0

    for x in range(1, total + 1):
        for coin in coins:
            if x >= coin:
                r[x] = min(r[x], r[x - coin] + 1)

    return r[total] if r[total] != float("infinity") else - 1
