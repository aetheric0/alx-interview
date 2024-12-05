#!/usr/bin/python3
""" Provides a function to calculate the
perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """ Calculates the perimeter of the island in the given grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
