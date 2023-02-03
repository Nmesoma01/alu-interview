#!/usr/bin/python3
"""
Minimum Operation"""

def minOperations(n):
    """Return 0 if n is less than or equal to 0"""
    if n <= 0:
        return 0

    operations = 0 """ Initialize the number of operations to 0"""

    for t in range(2, n/2):
        while(n % t == 0):
            operations += t """Increase the number of operations by 1"""
            n = n / t
    return(operations)
