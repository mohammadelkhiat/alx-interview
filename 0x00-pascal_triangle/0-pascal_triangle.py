#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[i - 1]
        # Start a new row with 1
        new_row = [1]

        # Compute the values for the middle of the row
        for j in range(1, i):
            # Each element is the sum of the two above it
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)

        # End the row with 1
        new_row.append(1)
        # Append the new row to the triangle
        triangle.append(new_row)

    return triangle
