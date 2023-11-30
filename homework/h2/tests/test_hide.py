"""
File: homework/h2/tests/test_hide.py
Initial contributor: Mihaela
Contributor: Justin Myshrall
Date: 10/27/23
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from src import linear_efficiency


class HideTestCases(unittest.TestCase):
    """
    Two test cases for `Hide` Function
    """

    def test_one(self):
        """
        Test's String "babble"
        """
        expected = 'ba**le'
        actual = hide('babble')
        self.assertEqual(actual, expected)

    def test_two(self):
        """
        Test's an empty string `""`
        """
        expected = ''
        actual = hide('')
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
