#!/usr/bin/python3

"""
this is a function that returns the perimeter
of the island described in grid
"""


def island_perimeter(grid):
    """
    method definition for a function
    that returns the island's perimeter
    """
    perimeter = 0
    rows, columns = len(grid), len(grid[0])

    for ro in range(rows):
        for co in range(columns):
            if grid[ro][co] == 1:
                perimeter += 4
                if ro > 0 and grid[ro - 1][co] == 1:
                    perimeter -= 2

                if co > 0 and grid[ro][co - 1] == 1:
                    perimeter -= 2
    return perimeter
