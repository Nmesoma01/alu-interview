#!/usr/bin/python3
"""
pascal's triangle
Generates Pascal's Triangle up to a given index.
"""


def pascal_triangle(n):
    """get pascal triangle to a certain index"""
def generate_pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []
    result = [[1], [1, 1]]
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        list_above = [0] + result[i - 1] + [0]
        prev_row = [0] + triangle[i - 1] + [0]
        row = []
        for j in range(0, len(list_above) - 1):
            row.append(list_above[j] + list_above[j + 1])
        result.append(row)
    return result[:n]
        for j in range(0, len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        triangle.append(row)
    return triangle[:n]
