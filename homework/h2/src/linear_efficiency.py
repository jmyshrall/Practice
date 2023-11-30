"""
File: homework/h2/src/linear_efficiency.py
Initial contributor: Mihaela
Contributor: Justin Myshrall
Date: 10/27/23

Implementation requirement:
- Apply the accumulation pattern
- Do not modify the values of the parameters
- Do not return a parameter
- If the use of a built-in data type method eliminates the use of the
    accumulation pattern in the design of a function, do not use it.
    Instead, write a 2nd design for that function to illustrate the use of
    built-in data type method.
"""


def hide(sentence):
    """
    Creates a new string with characters in `sentence` such that:
        - all subsequence occurrences of a character in `sentence` are
        replaced  with '*' in the returned sentence.
    :param sentence: string
    :return: string with the first occurrences of each character in `sentence`
        replaced by '*'
    :return: empty string or 1-character string identical with `sentence` if
        `sentence` is empty string or 1-character string
    Example 1: hide('babble') returns 'ba**le'
    Example 2: hide('more is less') returns 'more is*l***'
    """
    if len(sentence) <= 1:
        return sentence
        # If the input is an empty string or 1-character string

    seen_chars = set()
    # To keep track of characters that have been seen
    result = []
    for char in sentence:
        if char not in seen_chars:
            seen_chars.add(char)
            result.append(char)
        else:
            result.append('*')

    return ''.join(result)


def reduce_adjacent(num_lst):
    """
    Creates a new list with integers in `num_lst` such that:
        - adjacent integers that are the same in `num_lst` are replaced
        with one integer in the returned list.
    :param num_lst: list of integers
    :return: list of integers with no repeats
    :return: list of integers identical with `num_lst` if `num_lst` has no
        repeats
    Example: reduce_adjacent([1, 2, 2, 3]) returns [1, 2, 3]
    """
    if len(num_lst) <= 1:
        return num_lst
        # If the input list is empty or has only one element

    result = [num_lst[0]]
    # Initialize the result list with the first element of num_lst
    for num in num_lst[1:]:
        if num != result[-1]:
            # Compare with the last element in the result list
            result.append(num)

    return result


def reverse(word):
    """
    Creates and returns a new string that has the characters in `word`
    but in reverse order
    :param word: string
    :return: string with characters from `word` in reverse order
    :return: empty string if `word` is empty
    Example: reverse('python') returns 'nohtyp'
    Implementation requirements: do not use list method reverse
    """
    if not word:
        return ''
    # Check if the input word is empty
    result = ''
    # Initialize an empty string to store the reversed characters
    for char in word:
        result = char + result
        # Prepend each character to the result string

    return result
