"""
Author: Justin Myshrall
Date: 11/9/2023
"""


def factorial(n):
    """
    Calculates the factorial of a given non-negative integer using recursion.
    Param:
    - n (int): The non-negative integer for which the factorial is calculated.
    Return:
    - int: The factorial of the input integer.
    - time complexity: O(n)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# test case
result = factorial(7)
print(result)
