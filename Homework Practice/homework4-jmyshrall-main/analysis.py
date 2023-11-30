"""
File: analysis.py
Initial author: Mihaela
Developer: Justin Myshrall
Date: 4/18/2023
"""


class Analysis:
    """
    Analyze data recording study hours for individual students.
    Each line in the file has strings separated by commas:
        - 1st string is the name of the student
        - the following strings represent study hours
    Instance variables:
        self.file_in, string, name of the input file
        self.file_out, string, name of the output file
        self.Data, list of strings, each string correspond to a line in the
            input file.
    """

    def __init__(self, file_in, file_out='output.csv'):
        """
        Create Analysis object. Its instance variables have
        - the name of the input text file from where data is read
        - the name of the output text file where various outputs are right
        - the content of the input file.
        :param file_in: string        :param file_out:
        """
        self.file_in = file_in
        self.file_out = file_out
        with open(file_in, 'r') as f:
            self.Data = f.readlines()

    def transform_to_d(self):
        """
        Find the hours recorded for each student in `self.data`.
        :return: dictionary
            keys are strings, representing student names
            values are list of integers, corresponding to the study hours
        Example: If `self.data` has the content of 'data_2.csv`
            the method returns: {'joe':[10,8,5,10], 'sue':[7,9,10]}
        """
        hours_dict = {}
        for line in self.Data:
            line_list = line.strip().split(',')
            name = line_list[0]
            hours = [int(x) for x in line_list[1:]]
            hours_dict[name] = hours
        return hours_dict

    def avg_hours(self, student_hours_d):
        """
        Find the average number of study hours for each student.
        :param student_hours_d: dictionary
            keys are strings, representing student names
            values are list of integers, corresponding to the study hours
        :return: dictionary, keys are student names, values are hour averages.
        Example: if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
            the function returns {'joe':33, 'sue':26}
        """
        avg_dict = {}
        for name, hours in student_hours_d.items():
            avg_dict[name] = sum(hours) / len(hours)
        return avg_dict

    def min_max_hours(self, student_hours_d):
        """
        Find the minimum number of hours studied by each student.
        :param student_hours_d:
            keys are strings, representing student names
            values are list of integers, corresponding to the study hours
        :return: list of integers representing minimum number of hours studied
            by each student
        Example if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
            the function returns [5,7]
        """
        min_list = []
        for hours in student_hours_d.values():
            min_list.append(min(hours))
        return min_list

    def report_avg(self):
        """
        Write to `self.file_out` the average number of hours for each student.
        A line in the output file has the name of the student followed by
        one space and then the average number of hours.
        Example: if `self.data` had data from `data_2.csv`, the output file
        has the following content:
            joe 33
            sue 26
        """
        student_hours_d = self.transform_to_d()
        avg_dict = self.avg_hours(student_hours_d)
        with open(self.file_out, 'w') as f:
            for name, avg in avg_dict.items():
                f.write(f"{name} {avg}\n")
