> HW1 Design Document

## def count(num_list, num):
    """
    Find how many times `num` is in `num_list`.
    :param num_list: list of integers
    :param num: integer    :return: , representing how many times `num` is in `num_list`
    """
### Problem Solving Steps
- Take a list of integers and check if an integer `num` is contained in the list
- Do this by seeing if the current index of `num_list` is the same value as `num`
- If index == `num` then add one occurrence of `num` to `result` as type `int`
- And return `result` 

## def extend(num_list, another_num_list):
    """
    Build and return a new list that has the items in `num_list` followed by
    the items in `another_num_list` preserving the order.
    :param num_list: list of integers
    :param another_num_list: list of integers
    :return: list of integers
    """
### Problem Solving Steps
- Take original `num_list` and extend it using `another_num_list` 
- Since `.extend` method is not allowed `.append` will be used to concatenate both lists
- Take `num_list` append it to a final `result_list` at each index 
- Take `another_num_list` append it on the end of `result_list` at each index
- have the `another_num_list` at the end of `result_list` by appending after `num_list`
- return `result_list`

## def remove(num_list, num):
    """
    Build and return a new list that has the items in `num_list` in their
    original order, except for `num` item, which gets removed.
    :param num_list: list of integers
    :param num: integer
    :return: list of integers
    """
### Problem Solving Steps
- Remove a given `num` from `num_list` without using `.remove`
- Iterate through `num_list` using `for` loop 
- At each iteration check if the current index does not equal `num` using `!=`
- If the current index is not the same value as `num` then it will append to `result_list`
- Return `result_list`

## def index(num_list, num):
    """
    Find index of `num` in `num_list`.
    :param num_list: list of integers
    :param num: integer
    :return: non-negative integer of the index of the first current of
    `num`
    :return: None, if `num` not found
    """
### Problem Solving Steps
- Find the index of a given `num` in `num_list` and return value as type `int`
- Cannot use `.index` method, use `enumerate` to check current index and its value
- Iterate through `num_list` using 2 variables `idx`, `i` for index and value 
- If the current index value is = to `num` then the function will return the `idx` not `i`
- If the entire list passes with no match then function will return `None`
