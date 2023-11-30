"""
Test functions in olympics.py
File: test_olympics.py
Initial author: Mihaela
Contributor: Justin Myshrall
Collaborator(s): None
Date: 4/13/2023
"""
from olympics import *


def test_line_count():
    """
    Test the function using two test cases:
        `olympics_2.txt` and `olympics_4.txt` files
    """
    # first test case
    o_obj = Olympics('olympics_2.txt')
    print(o_obj.data)

    # second test case
    o_obj = Olympics('olympics_4.txt')
    print(o_obj.data)

def test_transform():
    """
    Test the function using two test cases:
        `olympics_2.txt` and `olympics_4.txt` files
    """
    # first test case
    o_obj = Olympics('olympics_2.txt')
    actual = o_obj.line_count()
    expected = 2
    print(f'actual is {actual}')
    print(f'expected is {expected}')

    # second test case
    o_obj = Olympics('olympics_4.txt')
    actual = o_obj.line_count()
    expected = 4
    print(f'actual is {actual}')
    print(f'expected is {expected}')

def test_report():
    """
    Test the function using two test cases:
        `olympics_1.txt` and `olympics_2.txt` files
    """
    # first test case

    # second test case


def test_report_to_file():
    """
    Test the function on 'olympics_4.txt' test case
    """


def main():
    """
    Call the testing functions defined in this module
    """
    test_line_count()
    test_transform()
    # test_report()
    # test_report_to_file()


main()
