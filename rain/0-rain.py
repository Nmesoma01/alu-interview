#!/usr/bin/python3
"""
Rain
"""

def rain(walls):
"""
Return total amount of rainwater retained.
"""
if not walls:
return 0

rainwater = 0
for i in range(len(walls)):
    if walls[i] == max(walls):
        continue

    max_lef = max(walls[:i])
    max_right = max(walls[i:])

    if max_lef > walls[i] and max_right > walls[i]:
        if max_lef < max_right:
            rainwater += max_lef - walls[i]
        else:
            rainwater += max_right - walls[i]
return rainwater
