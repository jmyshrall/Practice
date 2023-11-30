> Lab5 Design Document

## def get_average_for_all(self):
    """
    Returns the average ramen rating across ALL ratings
    :return: the average for ratings for the given country
    :rtype: float
    """
### Problem Solving Steps
- Initialize variables `total_ratings` and `total_stars` to 0.
- Iterate over each `ramen` entry in the `ramen_set`.
- For each entry, increment `total_ratings` and add the rating to `total_stars`.
- Calculate and return the average rating by dividing `total_stars` by `total_ratings`.

## def get_average_for_country(self, country):
    """
    Returns the average ramen rating for a given country
    :param country: the country for which the ratings belong to
    :type country: string
    :return: the average for ratings for the given country
    :rtype: float
    """
### Problem Solving Steps
- Initialize variables `total_ratings` and `total_stars` to 0.
- Iterate over each `ramen` entry in the `ramen_set`.
- For each entry from the specified country, increment `total_ratings` 
and add the rating to `total_stars`.
- Calculate and return the average rating by dividing `total_stars` by `total_ratings`.

## def get_percent_of_variety_that_include_the_word_ramen(self):
    """
    Returns the percentage of ramen variety that include the word "ramen"
    :return: the percentage of ramen variety that include the word "ramen"
    :rtype: float
    """
### Problem Solving Steps
- Initialize variables `total_ramen_with_word` and `total_varieties` to 0.
- Iterate over each `ramen` entry in the `ramen_set`.
- For each entry, check if the word "ramen" is in the variety name (case-insensitive).
- If true, increment `total_ramen_with_word`.
- Increment `total_varieties` for each entry.
- Calculate and return the percentage by dividing `total_ramen_with_word`
by `total_varieties` and multiplying by 100.

## def get_ramen_by_country(self):
    """
    Returns a dictionary with the ramen categorized by country
    :return:  dict with keys being the country name and values being
        a list of ramen for that country
        ex: {'USA': [[2580, 'New Touch', "T's Restaurant', 'Cup', 'etc]]
    :rtype: dictionary
    """
### Problem Solving Steps
- Initialize an empty dictionary `ramen_categorized`.
- Iterate over each ramen entry in the `ramen_set`.
- For each entry, get the country name and add the entry to the 
corresponding list in `ramen_categorized`.
- Return the `ramen_categorized` dictionary.