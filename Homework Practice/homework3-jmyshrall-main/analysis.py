"""
File: analysis.py
Initial author: Mihaela
Contributor: Justin Myshrall
Date: 4/11/2023
"""


def read_data(filename):
    """
    Read the text file named filename to report the hours recorded for each
    student in the file. Each file line has strings separated by commas:
    - 1st string is the name of the student
    - the following strings represent study hours
    :param filename: str, name of the file
    :return: dictionary
        keys are strings, representing student names
        values are list of integers, corresponding to the study hours
    Example: If filename is `data_2.csv`,
        the function returns: {'joe':[10,8,5,10], 'sue':[7,9,10]}
    """
    data = {}
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split(',')
            name = fields[0]
            hours = [int(h) for h in fields[1:]]
            data[name] = hours
    return data


def sum_hours(filename):
    """
    Find the total number of study hours for each student.
    :param filename: dictionary
        keys are strings, representing student names
        values are list of integers, corresponding to the study hours
    :return: dictionary, keys are student names, values are hour averages.
    Example: if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
        the function returns {'joe':33, 'sue':26}
    """
    total_hours = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.split(',')
            name = data[0]
            hours_list = [int(h) for h in data[1:]]
            total_hours[name] = sum(hours_list)
    return total_hours


def min_max_hours(filename):
    """
    Find the minimum number of hours studied by each student.
    :param filename:
        keys are strings, representing student names
        values are list of integers, corresponding to the study hours
    :return: list of integers representing minimum number of hours studied by
        each student
    Example if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
        the function returns [5,7]
    """
    min_hours = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split(',')
            hours_list = [int(h) for h in data[1:] if h]
            if hours_list:
                min_hours.append(min(hours_list))
            else:
                min_hours.append(0)
    return min_hours
