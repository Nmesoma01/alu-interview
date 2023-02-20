#!/usr/bin/python3
"""
Rain
"""


def rain(walls):
    """
    Return total amount of water retained.
    """
    if not walls:
        return 0

    water = 0
    for i in range(len(walls)):
        if walls[i] != max(walls):
            max_lef = 0
            max_right = 0
            for j in range(0, i):
                if max_lef < walls[j]:
                    max_lef = walls[j]
            for k in range(i, len(walls)):
                if max_right < walls[k]:
                    max_right = walls[k]
            if max_lef != 0 and max_right != 0:
                if max_lef < max_right and max_lef > walls[i]:
                    water += max_lef - walls[i]
                elif max_right <= max_lef and max_right > walls[i]:
                    water += max_right - walls[i]
    return water
