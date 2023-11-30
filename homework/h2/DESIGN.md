> HW2 Design Document

## def hide(sentence):
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
### Problem Solving Steps
- Check the length of the input sentence:
    If `len` is less than or equal to 1, return the `sentence` as is.
    Initialize a set called `seen_chars` to keep track of characters 

- Create an empty list called `result` to build the final `result`.

  - Iterate through each `char` in the input `sentence` using a `for` loop:
        For each character, check if it's in the `seen_chars` set:
            - If the character is not in the set, mark it as seen by adding it to `seen_chars` 
            and append it to the `result`.
            - If the character is already in the set, represent it with an `*` in the `result`.
  - After processing all `char`, use the `.join()` method to concatenate 
  the characters in the `result` into a single string.
Return the modified string as the final `result`.

## def reduce_adjacent(num_lst):
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
### Problem Solving Steps
- Check the length of the `input_list` `num_lst`:
    If the length of `num_lst` is less than or equal to 1, return `num_lst` as is.
    This handles the case of an empty list or a list with just one element.
- Initialize a list called `result` with the first element of `num_lst`:
  The `result` is initialized with the first element of the `input_list` to ensure 
  that at least one element is included in the `result`.
  Iterate through the elements of `num_lst` starting from the second element using a for loop:
- For each element, compare it with the last element in the result list `result[-1]`:
  If the current element is different from the last element in the `result` list, it means it's not a duplicate.
  Append the current element to the `result` list.
- return the `result` list

## def reverse(word):
    """
    Creates and returns a new string that has the characters in `word`
    but in reverse order
    :param word: string
    :return: string with characters from `word` in reverse order
    :return: empty string if `word` is empty
    Example: reverse('python') returns 'nohtyp'
    Implementation requirements: do not use list method reverse
    """
### Problem Solving Steps
- Check if the `input_word` is empty:
    If `word` is empty, return an empty string as the `result`.

- Initialize an empty string called `result` to store the reversed `char`.
    Iterate through each `char` in the `input_word` using a for loop:
        For each character, prepend it to the `result` string.
- return the `result string`