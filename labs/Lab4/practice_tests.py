"""
test_parse_season.py
Mihaela
Created March 20, 2019. Updated October 15, 2019
"""

import unittest
from practice_dictionaries import Practice


class TestParseSeasons(unittest.TestCase):
    """
    Tests for parse_seasons() method
    """

    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.p = Practice()

    def test_brief_descriptions(self):
        """
        Test case with short season descriptions
        """
        input1 = {
            'spring': 'warm',
            'summer': 'hot',
            'fall': 'justright',
            'winter': 'cold'
        }
        actual_result = self.p.parse_seasons(input1)
        expected_result = 'springwarmsummerhotfalljustrightwintercold'
        self.assertEqual(actual_result, expected_result)

    def test_update_inventory(self):
        """
        Test the update_inventory method
        """
        inventory_dict = {
            "item1": 10,
            "item2": 5,
            "item3": 20,
        }
        quantity_added = 3
        expected_result = {
            "item1": 13,
            "item2": 8,
            "item3": 23,
        }
        actual_result = self.p.update_inventory(inventory_dict, quantity_added)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
