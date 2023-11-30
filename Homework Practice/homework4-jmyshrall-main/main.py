"""
File: main.py
Initial author: Mihaela
Developer: Justin Myshrall
Date: 4/18/2023
"""
from analysis import Analysis


def demo_transform_to_d():
    """
    Demo the method on three test cases, 'data_1.csv', 'data_2.csv', and
    'data_5.csv'
    """
    analysis_1 = Analysis('data_1.csv')
    result_1 = analysis_1.transform_to_d()
    print(result_1)

    analysis_2 = Analysis('data_2.csv')
    result_2 = analysis_2.transform_to_d()
    print(result_2)

    analysis_5 = Analysis('data_5.csv')
    result_3 = analysis_5.transform_to_d()
    print(result_3)


def demo_avg_hours():
    """
    Demo the method on two test cases, 'data_1.csv', 'data_2.csv', and
    'data_5.csv'
    """
    analysis_1 = Analysis('data_1.csv')
    student_hours_1 = analysis_1.transform_to_d()
    result_1 = analysis_1.avg_hours(student_hours_1)
    print(result_1)

    analysis_2 = Analysis('data_2.csv')
    student_hours_2 = analysis_2.transform_to_d()
    result_2 = analysis_2.avg_hours(student_hours_2)
    print(result_2)

    analysis_5 = Analysis('data_5.csv')
    student_hours_5 = analysis_5.transform_to_d()
    result_3 = analysis_5.avg_hours(student_hours_5)
    print(result_3)


def demo_min_max_hours():
    """
    Demo the method on two test cases, 'data_1.csv', 'data_2.csv', and
    'data_5.csv'
    """
    analysis_1 = Analysis('data_1.csv')
    student_hours_1 = analysis_1.transform_to_d()
    result_1 = analysis_1.min_max_hours(student_hours_1)
    print(result_1)

    analysis_2 = Analysis('data_2.csv')
    student_hours_2 = analysis_2.transform_to_d()
    result_2 = analysis_2.min_max_hours(student_hours_2)
    print(result_2)

    analysis_5 = Analysis('data_5.csv')
    student_hours_5 = analysis_5.transform_to_d()
    result_3 = analysis_5.min_max_hours(student_hours_5)
    print(result_3)


def demo_report_avg():
    """
    Demo the method on two test cases, 'data_1.csv', 'data_2.csv', and
    'data_5.csv'. This demo is different from the previous ones. Each case
    uses a different output file name, 'output_1.txt', 'output_2.txt', and
    'output_5.txt'. After each `Analysis` object is created, simply call the
    method to generate the output text file. Its content shows whether the
    method is designed and implemented correctly.
    """
    analysis_1 = Analysis('data_1.csv', 'output_1.txt')
    analysis_1.report_avg()

    analysis_2 = Analysis('data_2.csv', 'output_2.txt')
    analysis_2.report_avg()

    analysis_5 = Analysis('data_5.csv', 'output_5.txt')
    analysis_5.report_avg()


def main():
    """
    Demonstrate all methods
    """
    # Call all demo functions. Have all the calls commented out, except for
    # the function you are currently demonstrating.

    demo_transform_to_d()

    # demo_avg_hours()

    # demo_min_max_hours()

    # demo_report_avg()


main()
