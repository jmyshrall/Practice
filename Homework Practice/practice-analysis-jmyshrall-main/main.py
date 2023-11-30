"""
File: main.py
Initial author: Mihaela
Developer: Justin Myshrall
Collaborator: None
Date: 4/20/2023
"""
from analysis import *


def test_read_data():
    """
    Test the function read_data()
    """
    expected = [{'loan': 1250.0, 'country': 'Azerbaijan', 'raising_time': 193075, 'lenders': 38}]
    actual = read_data('data_1.csv')
    print(f'expected is {expected}')
    print(f'actual is {actual}')

    expected = [{'loan': 1250.0, 'country': 'Azerbaijan', 'raising_time': 193075, 'lenders': 38}], \
        [{'loan': 500.0, 'country': 'El Salvador', 'raising_time': 1157108, 'lenders': 18}], \
        [{'loan': 1450.0, 'country': 'Bolivia', 'raising_time': 1552939, 'lenders': 51}], \
        [{'loan': 200.0, 'country': 'Paraguay', 'raising_time': 244945, 'lenders': 3}], \
        [{'loan': 700.0, 'country': 'El Salvador', 'raising_time': 238797, 'lenders': 21}]
    actual = read_data('data_5.csv')
    print(f'expected is {expected}')
    print(f'actual is {actual}')

    actual = read_data('data_25.csv')
    print(f'actual is {actual}')


def test_total_loan_amount():
    """
    Test the function `total_loan_amount()`
    """


def test_avg_lenders_per_loan():
    """
    Test the function `avg_lenders_per_loan()`
    """


def main():
    """
    Call the testing functions defined in this module
    """
    test_read_data()


main()
