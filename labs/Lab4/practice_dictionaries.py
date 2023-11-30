"""
practice_dictionaries.py
Get familiar with dictionaries
Mihaela Sabin
Created March 20, 2019
Updated October 16, 2019; February 19, 2020
"""


class Practice(object):
    """
    Illustrate methods that transform an input dictionary into some output
    """

    @staticmethod
    def parse_seasons(season_dict):
        """
        Create a string with info from season_dict
        season_dict: dictionary
            keys: strings - season names
            values: strings - season descriptions
        Returns: string with season names and descriptions and no spaces or
            other characters in between
        """
        season_info = ""
        for season, description in season_dict.items():
            season_info += season + description
        return season_info
        pass

    @staticmethod
    def update_inventory(inventory_dict, quantity_added):
        """
        Returns new dictionary with quantities for each item in inventory_dict
            increased by quantity-added
        inventory_dict: dictionary
            keys: strings - inventory item names
            values: int - inventory quantity of item
        Returns: dictionary
        """
        updated_inventory = {}
        for item, quantity in inventory_dict.items():
            updated_inventory[item] = quantity + quantity_added
        return updated_inventory
        pass


if __name__ == '__main__':
    p = Practice()
    input1 = {
        'spring': 'warm',
        'summer': 'hot',
        'fall': 'just right',
        'winter': 'cold'
    }
    result = p.parse_seasons(input1)
    print(f'parse_seasons({input1}) returns {result}')
