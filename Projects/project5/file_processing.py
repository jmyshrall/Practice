"""
Learn and practice text file processing.
File: comp424/project5/file_processing.py
Initial author: Mihaela
Developer: Justin Myshrall
Date: 3/30/2023
"""


def line_count(filename):
    """
    Find and return the number of lines in the file named `filename`
    :param filename: string
    :return: non-negative integer
    """
    with open(filename, 'r') as f_in:
        lines_list = f_in.readlines()
    total_line = 0
    for _ in lines_list:
        total_line = total_line + 1
    return total_line


def country_count(filename):
    """
    Find and return the number of countries in the file named `filename`. A
    country name starts at the beginning of a line in the file, ends with ':',
    and is separated from the rest of the characters in the line by a space.
    :param filename: string
    :return: mon-negative integer
    """
    count = 0
    with open(filename, 'r') as f_in:
        for line in f_in:
            if ':' in line:
                count += 1
    return count


def olympics_transform(filename):
    """
    Read and process the content of the text file `filename` to produce a tuple
    of 3 parallel lists. The first list has the name of the olympians, their
    age, and country of origin.
    :param filename: string
    :return: tuple of three parallel lists
        1st list is a list of strings, 2nd list is a list of integers, and
        3rd list is a list of strings.
    """
    names = []
    ages = []
    countries = []
    with open(filename, 'r') as f_in:
        for line in f_in:
            fields = line.split(',')
            name = fields[0]
            age = int(fields[2])
            country = fields[3]
            countries.append(country)
            names.append(name)
            ages.append(age)
    return names, ages, countries


def olympics_report(filename):
    """
    Read and process the content of the text file named `filename` to produce
    a string with given formatting requirements. For each line in the file
    produce a string that has the following format:
        <name> is from <country> and competes in <sport>
        where <name>, <country>, and <sport> are strings found in the line of
        the file.
    :param filename: string
    :return: list of strings
    """
    with open(filename, 'r') as f_in:
        lines = f_in.readlines()

    report = []
    for line in lines:
        fields = line.split(',')
        name = fields[0]
        country = fields[3]
        sport = fields[4]
        report.append(f"{name} is from {country} and competes in {sport}")
    return report
