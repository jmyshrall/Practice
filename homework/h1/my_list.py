"""
File: homework/h1/src/my_list.py
Initial contributor: Mihaela
Contributor: Justin Myshrall
Date: 10/5/2023

Implementation requirement:
- Do not call built-in list methods, except for append()
"""


def count(num_list, num):
    """
    Find how many times `num` is in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: , representing how many times `num` is in `num_list`
    """
    result = 0
    for i in num_list:
        if i == num:
            result += 1
    return result


def extend(num_list, another_num_list):
    """
    Build and return a new list that has the items in `num_list` followed by
    the items in `another_num_list` preserving the order.
    :param num_list: list of integers
    :param another_num_list: list of integers
    :return: list of integers
    """
    result_list = []
    for i in num_list:
        result_list.append(i)
    for i in another_num_list:
        result_list.append(i)
    return result_list


def remove(num_list, num):
    """
    Build and return a new list that has the items in `num_list` in their
    original order, except for `num` item, which gets removed.
    :param num_list: list of integers
    :param num: integer
    :return: list of integers
    """
    result_list = []
    for i in num_list:
        if i != num:
            result_list.append(i)
    return result_list


def index(num_list, num):
    """
    Find index of `num` in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: non-negative integer of the index of the first current of
    `num`
    :return: None, if `num` not found
    """
    for idx, i in enumerate(num_list):
        if i == num:
            return idx
    return None


def test_count():
    """
    Uses 2 tests for `count()` function
    """
    # test 1
    num_list = [1, 2, 3, 2, 4, 2, 5]
    num = 2
    count_integer = count(num_list, num)
    print(f"{num} appears {count_integer} times in the list.")

    # test 2
    num_list = [1, 2, 3, 2, 4, 2, 5]
    num = 5
    count_integer = count(num_list, num)
    print(f"{num} appears {count_integer} times in the list.")


def test_extend():
    """
    Uses 2 tests for `extend()` function
    """
    # test 1
    num_list = [1, 2, 3, 2, 4, 2, 5]
    another_num_list = [6, 7, 8]
    extended_list = extend(num_list, another_num_list)
    print(extended_list)

    # test 2
    num_list = [1, 2, 3, 2, 4, 2, 5]
    another_num_list = [4, 3, 2, 1]
    extended_list = extend(num_list, another_num_list)
    print(extended_list)


def test_remove():
    """
    Uses 2 tests for `remove()` function
    """
    # test 1
    num_list = [1, 2, 3, 2, 4, 2, 5]
    num = 2
    remove_list = remove(num_list, num)
    print(remove_list)

    # test 2
    num_list = [1, 2, 3, 2, 4, 2, 5]
    num = 5
    remove_list = remove(num_list, num)
    print(remove_list)


def test_index():
    """
    Uses 2 tests for `index()` function
    """
    # test 1
    num_list = [1, 2, 3, 4, 2, 5]
    num = 2
    index_integer = index(num_list, num)
    if index_integer is not None:
        print(f"The index of {num} in the list is {index_integer}.")
    else:
        print(f"{num} is not found in the list.")

    # test 2
    num_list = [1, 2, 3, 4, 2, 5]
    num = 6
    index_integer = index(num_list, num)
    if index_integer is not None:
        print(f"The index of {num} in the list is {index_integer}.")
    else:
        print(f"{num} is not found in the list.")


def main():
    """
    Call the testing functions defined in this module
    """
    test_count()

    test_extend()

    test_remove()

    test_index()


main()
