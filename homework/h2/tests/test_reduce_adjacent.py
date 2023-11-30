"""
File: homework/h2/tests/test_reduce_adjacent.py
Initial contributor: Mihaela
Contributor: Justin Myshrall
Date: 10/27/2023
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency


class TestReduceAdjacentFunction(unittest.TestCase):
    """
    Two test cases for `reduce_adjacent` Function
    """
    def test_reduce_adjacent_example_1(self):
        """
        test one
        """
        input_list = [1, 2, 2, 3]
        expected = [1, 2, 3]
        actual = reduce_adjacent(input_list)
        self.assertEqual(actual, expected)

    def test_reduce_adjacent_example_2(self):
        """
        test two
        """
        input_list = [4, 4, 4, 4, 4]
        expected = [4]
        actual = reduce_adjacent(input_list)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
