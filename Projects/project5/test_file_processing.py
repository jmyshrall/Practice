"""
Test functions in file_processing.py
"""
from file_processing import *


def test_line_count():
    """
    Test the function using two test cases:
        `travel_log.txt` and `travel_empty.txt` files
    """
    # first test case
    filename = 'travel_log.txt'
    actual = line_count(filename)
    expected = 8
    print(actual)
    print(expected)

    # second test case
    filename = 'travel_empty.txt'
    actual = line_count(filename)
    expected = 0
    print(actual)
    print(expected)


def test_country_count():
    """
    Test the function using the file `travel_log.txt`
    """
    # first test case
    filename = 'travel_log.txt'
    actual = country_count(filename)
    expected = 6
    print(actual)
    print(expected)

    # second test case
    filename = 'travel_empty.txt'
    actual = country_count(filename)
    expected = 0
    print(actual)
    print(expected)

def test_olympics_transform():
    """
    Test the function using `olympics_4.txt` file
    """
    # first test case
    filename = 'olympics_2.txt'
    actual = olympics_transform(filename)
    print(actual)

    # second test case
    filename = 'olympics_4.txt'
    actual = olympics_transform(filename)
    print(actual)


def test_olympics_report():
    """
    Test the function using the `olympics_2.txt` file.
    """
    # first test case
    filename = 'olympics_2.txt'
    actual = olympics_report(filename)
    print(actual)

    # second test case
    filename = 'olympics_4.txt'
    actual = olympics_report(filename)
    print(actual)

def main():
    """
    Call the testing functions defined in this module
    """
    test_line_count()

    test_country_count()

    test_olympics_transform()

    test_olympics_report()


main()
