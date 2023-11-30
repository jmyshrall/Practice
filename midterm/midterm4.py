"""
Author: Justin Myshrall
Date: 11/9/2023
"""


class Stack:
    """
    constructor for a stack
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def string_reverse(input_string):
    """
    Reverses a string using a Stack.
    Param:
    - input_string (str): The input string to be reversed.
    Return:
    - str: The reversed string.
    - time complexity: O(n)
    """
    stack = Stack()
    for char in input_string:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string


# test case
result = string_reverse("I really love data structures")
print(result)
