"""
File: homework/h2/tests/test_reverse.py
Initial contributor: Mihaela
Contributor: Justin Myshrall
Date: 10/27/2023
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from src import test_reverse


class TestReverseFunction(unittest.TestCase):
    """
    Two test cases for `reverse` Function
    """
    def test_reverse_example_1(self):
        """
        test one
        """
        input_word = 'python'
        expected = 'nohtyp'
        actual = reverse(input_word)
        self.assertEqual(actual, expected)

    def test_reverse_empty_string(self):
        """
        test two empty string `""`
        """
        input_word = ""
        expected = ""
        actual = reverse(input_word)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
