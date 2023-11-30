"""
Author: Justin Myshrall
Date: 11/9/2023
"""

def sort_strings_by_length(input_list):
    """
    Sorts a list of strings based on the length of the strings.
    Param:
    - input_list (list): The list of strings to be sorted.
    Return:
    - list: The sorted list of strings.
    - time complexity: o(nlog(n))
    """
    sorted_list = sorted(input_list, key=len)
    return sorted_list


# test case
input_strings = ["apple", "banana", "cherry", "date"]
result = sort_strings_by_length(input_strings)
print(result)
