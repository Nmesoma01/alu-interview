#!/usr/bin/python3
"""minimum operations file"""


def minOperations(n):
    """Return 0 if n is less than or equal to 0"""
    if not n or n < 2:
        return 0
    numberOperations = 0
    for time in range(2, n+1):
        while(n % time == 0):
            numberOperations += time
            n = n / time
    return(numberOperations)
