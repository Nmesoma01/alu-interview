def pascal_triangle(n):
    """
    Compute and return the Pascal's triangle of size `n`.
    If `n` is not positive, return an empty list.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row, which is just [1]
    triangle = [[1]]

    # Iterate from 1 to n-1 to compute each subsequent row
    for i in range(1, n):
        # Initialize a new list for the current row, with a 1 at the beginning
        row = [1]

        # Iterate from 1 to i-1 to compute the values in the middle of the row
        for j in range(1, i):
            # Compute the value in the middle of the row by summing the corresponding values from the previous row
            # The value at position (i-1, j-1) corresponds to the left neighbor, and the value at position (i-1, j) corresponds to the right neighbor
            middle_value = triangle[i-1][j-1] + triangle[i-1][j]
            # Append the middle value to the current row
            row.append(middle_value)

        # Append another 1 at the end of the row
        row.append(1)

        # Append the completed row to the triangle list
        triangle.append(row)

    # Return the completed triangle
    return triangle
