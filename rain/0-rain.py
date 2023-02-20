#!/usr/bin/python3
"""
calculate how many square units of water will be retained after it rains
"""
def rain(walls):
    """
    Provide the cumulative volume of water that has been held or trapped.
    """
    if not walls:
        return 0

    water = 0
    for i in range(len(walls)):

        if walls[i] != max(walls):
            max_left = 0
            max_right = 0
            for j in range(0, i):
                if max_left < walls[j]:
                    max_left = walls[j]

            for k in range(i, len(walls)):
                if max_right < walls[k]:
                    max_right = walls[k]
            if max_left != 0 and max_right != 0:
                if max_left < max_right and max_left > walls[i]:
                    water += max_left - walls[i]
                elif max_right <= max_left and max_right > walls[i]:
                    water += max_right - walls[i]
    
    return water
