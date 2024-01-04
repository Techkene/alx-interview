#!/usr/bin/python3
"""A script to determine Pascal's triangle for any number"""

def calculate_binomial_coefficient(n, k):
    """Calculates the binomial coefficient (n choose k)"""
    if k == 0 or k == n:
        return 1
    else:
        return calculate_binomial_coefficient(n - 1, k - 1) + calculate_binomial_coefficient(n - 1, k)

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    for i in range(n):
        row = [calculate_binomial_coefficient(i, j) for j in range(i + 1)]
        triangle.append(row)

    return triangle
