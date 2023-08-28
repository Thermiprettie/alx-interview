#!/usr/bin/python3

""" Function that returns the perimiter of an island """


def island_perimeter(grid):
    """
    Returns the Perimeter of the island described in grid
    """
    tot = 0
    wdth = len(grid)
    hgth = len(grid[0]) if wdth else 0

    for t in range(len(grid)):
        for v in range(len(grid[t])):

            sth = [(t - 1, v), (t, v - 1), (t, v + 1), (t + 1, v)]
            st8 = [1 if s[0] in range(wdth) and s[1] in range(hgth) else 0
                     for s in sth]

            if grid[t][v]:
                tot += sum([1 if not b or not grid[s[0]][s[1]] else 0
                              for b, s in zip(st8, sth)])

    return (tot)
