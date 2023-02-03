#!/usr/bin/python3

"""minimum operations file"""


def minOperations(n):
    """ Return 0 if n is less than or equal to 0"""
    if n <= 0:
        return 0

    numberofoperations = 0  """ Initialize the num of operations to 0  """

    while n != 1:
        if n % 2 == 0: """ Check if n is a multiple of 2 """
            n = n // 2 
            numberofoperations += 1  """ Increase the num of operations by 1 """
        else:
            return 0 """ If n is not divisible by 2, it's impossible to achieve n H's """

     """ Return the total number of operations """
    return numberofoperations
