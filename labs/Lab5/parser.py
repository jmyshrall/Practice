"""
Parser for Ramen Stats
Jon
Contributor: Justin Myshrall
20211210
"""
import csv


class RamenStats:
    """
    Ramen stats provide interface for reading and parsing ramen stats
    """

    file_name = 'ramen.csv'

    def __init__(self):
        """
        Constructor
        """
        self.ramen_set = []
        with open(self.file_name, 'r', encoding='UTF-8') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                self.ramen_set.append(row)

    def get_average_for_all(self):
        """
        Returns the average ramen rating across ALL ratings
        :return: the average for ratings for the given country
        :rtype: float
        """
        total_ratings = 0
        total_stars = 0
        for ramen in self.ramen_set:
            total_ratings += 1
            total_stars += float(ramen['Stars'])
        if total_ratings == 0:
            return 0
        return total_stars / total_ratings

        pass

    def get_average_for_country(self, country):
        """
        Returns the average ramen rating for a given country
        :param country: the country for which the ratings belong to
        :type country: string
        :return: the average for ratings for the given country
        :rtype: float
        """
        total_ratings = 0
        total_stars = 0
        for ramen in self.ramen_set:
            if ramen['Country'] == country:
                total_ratings += 1
                total_stars += float(ramen['Stars'])
        if total_ratings == 0:
            return 0
        return total_stars / total_ratings

        pass

    def get_percent_of_variety_that_include_the_word_ramen(self):
        """
        Returns the percentage of ramen variety that include the word "ramen"
        :return: the percentage of ramen variety that include the word "ramen"
        :rtype: float
        """
        total_ramen_with_word = 0
        for ramen in self.ramen_set:
            if 'ramen' in ramen['Variety'].lower():
                total_ramen_with_word += 1
        if not self.ramen_set:
            return 0
        return (total_ramen_with_word / len(self.ramen_set)) * 100
        pass

    def get_ramen_by_country(self):
        """
        Returns a dictionary with the ramen categorized by country
        :return:  dict with keys being the country name and values being
            a list of ramen for that country
            ex: {'USA': [[2580, 'New Touch', "T's Restaurant', 'Cup', 'etc]]
        :rtype: dictionary
        """
        categorized = {}
        for ramen in self.ramen_set:
            country = ramen['Country']
            if country not in categorized:
                categorized[country] = []
            categorized[country].append(list(ramen.values()))
        return categorized
        pass


if __name__ == "__main__":
    stats = RamenStats()

    # average all expected to be ???
    print(f"Average All: {stats.get_average_for_all():.2f}")

    # average USA expected to be ???
    print(f"Average USA: {stats.get_average_for_country('USA'):.2f}")

    # Num ramen with "ramen" in their variety expected to be ???
    percent_ramen = stats.get_percent_of_variety_that_include_the_word_ramen()
    print(f"Variety % ramen: {percent_ramen:.2f}")

    # Num ramen for Japan expected to be ???
    ramen_categorized = stats.get_ramen_by_country()
    print(f"Num ramen for Japan: {len(ramen_categorized['Japan'])}")
