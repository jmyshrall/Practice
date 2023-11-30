"""
Learn and practice object-oriented programming using Olympics text file data.
Olympics dataset is organized by lines. Each line has the name of the olympian,
followed by gender, age, country, sport, and medal (or 'NA' if no medal).
File: comp424/practice-more/olympics.py
Initial author: Mihaela
Developer: Justin Myshrall
Collaborator(s): none
Date: 4/13/2023
"""
class Olympics:
    """
    """
    def __init__ (self, filename_in, filename_out = 'output.txt'):
        """
        Create object by getting data from `filename_in`, write output to `filename_out`, and store data
        into `self.data` list of strings
        :param filename_in: string :param filename_out: string
        """
        self.file_in = filename_in
        self.file_out = filename_out
        self.data = []
        with open(self.file_in, 'r') as f_in:
            self.data = f_in.readlines()

    def line_count(self):
        """
        Find and return the number of lines in the file named `filename`
        :return: non-negative integer
        """
        lines = len(self.data)
        return lines

    def transform(self):
        """
        Produce a tuple of 3 parallel lists using the file data.
        The first list has the names of the olympians, the 2nd list has their
        age, and the 3rd list has their countries.
        of origin.
        :return: tuple of three parallel lists
            1st list is a list of strings, 2nd list is a list of integers, and
            3rd list is a list of strings.
        """


    def report(self):
        """
        Produce a string with given formatting requirements using the data in
        the file. For each line, create a string that has the following format:
            <name> is from <country> and competes in <sport>\n
        where <name>, <country>, and <sport> are strings corresponding to data
        found in each of file lines.
        :return: list of strings
        """


    def report_to_file(self):
        """
        Call report() and write the return string to an output file
        """
