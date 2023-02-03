#!/usr/bin/python3
"""minimum operations file"""


def minOperations(n):
    # Return 0 if n is less than or equal to 0
    if n <= 0:
        return 0
    operations = 0 # Initialize the number of operations to 0
    while n != 1:
        if n % 2 == 0: # Check if n is divisible by 2
            n = n // 2 # Divide n by 2
            operations += 1 # Increment the number of operations by 1
        else:
            return 0 
    return operations
