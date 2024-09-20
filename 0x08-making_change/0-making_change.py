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

    for coin in coins:
        for x in range(coin, total + 1):
            r[x] = min(r[x], r[x - coin] + 1)

    return r[total] if r[total] != float("infinity") else - 1
