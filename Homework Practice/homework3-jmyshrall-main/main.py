"""
File: main.py
Initial author: Mihaela
Contributor: Justin Myshrall
Date: 4/11/2023
"""
from analysis import *


def main():
    """
    Demonstrate the functions in analysis.py
    """
    # test 1.1
    result = read_data('data_1.csv')
    print(result)

    # test 1.2
    result = read_data('data_2.csv')
    print(result)

    # test 1.3
    result = read_data('data_5.csv')
    print(result)

    # test 2.1
    result = sum_hours('data_1.csv')
    print(result)

    # test 2.2
    result = sum_hours('data_2.csv')
    print(result)

    # test 2.3
    result = sum_hours('data_5.csv')
    print(result)

    # test 3.1
    result = min_max_hours('data_1.csv')
    print(result)

    # test 3.2
    result = min_max_hours('data_2.csv')
    print(result)

    # test 3.3
    result = min_max_hours('data_5.csv')
    print(result)


main()
