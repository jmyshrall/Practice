"""
Author: Justin Myshrall
Date: 11/9/2023
"""
def check_even(input_list):
    """
    Write a Python function that takes a list of integers as input and returns
    a new list with only the even numbers. For example, if the input is [1, 2, 3, 4, 5, 6],
    the function should return [2, 4, 6].
    time complexity: O(n)
    """
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


# test case
input_numbers = [1, 2, 3, 4, 5, 6]
result = check_even(input_numbers)
print(result)
