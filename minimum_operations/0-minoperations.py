#!/usr/bin/python3

"""minimum operations file"""


def minOperations(n):
    # Return 0 if n is less than or equal to 0
    if n <= 2:
        return 0
    
    operations = 0 # Initialize the number of operations to 0
    
    # Keep dividing n by 2 until it becomes 1
    while n != 2:
        if n % 2 == 0: # Check if n is divisible by 2
            n = n // 2 # Divide n by 2
            operations += 2 # Increment the number of operations by 1
        else:
            return 0 # If n is not divisible by 2, it's impossible to achieve n H's
    
    # Return the total number of operations
    return operations
