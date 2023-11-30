"""
Solve Parsons Problems and computational problems to learn how to:
- document, test, design, implement, and debug functions.
File: comp424/homework2/lists_and_strings.py
Initial author: Mihaela
Developer: Justin Myshrall
Date: 3/2/2023
"""


def how_often(subject_log, subject):
    """
    Find out how many times `subject` is in `subject_log`.
    The subject log is kept every week to record the study sessions
    associated with various subjects. Thus, a subject might appear multiple
    times in the `subject_log` if there are multiple study sessions for that
    subject during the week. The order of the subjects is the chronological
    order of studying for those  subjects.
    :param subject_log: list of strings, representing subjects,
        e.g., ['comp', 'math', 'eng', 'comp']
    :param subject: string, e.g., 'bus'
    :return: integer, representing how many times `subject` is found in the
    `study_log`. May return 0 if `subject` is not found.
    Example: how_often(['comp, 'math', 'eng', 'comp'], 'comp') returns 2
    """
    result = 0
    for s in subject_log:
        if s == subject:
            result += 1
    return result


def subject_study_hours(subject_log, hour_log, subject):
    """
    Calculate the total number of study hours for `subject`.
    :param subject_log: list of strings representing subjects that correspond
    to weekly study sessions. Each occurrence of a subject has also a
    corresponding number of study hours in the `hour_log`.
    :param hour_log: list of integers representing study hours corresponding
    to each subject in the subject_log, e.g., [1, 3, 2]
    :param subject: string, representing a subject
    :return: integer
    Example: course_study_hours(['comp', 'math', 'comp'], [1, 3, 2], 'comp')
        returns 3
    """
    result = 0
    for s in range(len(subject_log)):
        if subject_log[s] == subject:
            result += hour_log[s]
    return result


def most_hours(subject_log, hour_log):
    """
    Find the subject with the largest number of hours studied in a session.
    :param subject_log: list of strings representing subjects that correspond
    to weekly study sessions. Each occurrence of a subject has also a
    corresponding number of study hours in the `hour_log`.
    :param hour_log: list of integers representing study hours corresponding
    to each subject in the subject_log
    :return: string, the subject with the largest number of hours
    Example: most_hours(['comp', 'math', 'comp'], [1, 3, 2]) returns 'math'
    Note: We assume that the maximum number of course in `hour_log` is unique.
    """
    max_hours = 0
    result = ''
    for i in range(len(subject_log)):
        if hour_log[i] > max_hours:
            max_hours = hour_log[i]
            result = subject_log[i]
    return result


def main():
    """
    Test the functions defined in this module.
    """
    # Write TWO tests for how_often()
    subject_log_ex = ['comp', 'math', 'eng', 'comp']
    subject_ex = 'comp'
    result = how_often(subject_log_ex, subject_ex)
    print(result)

    subject_log_ex = ['comp', 'math', 'eng', 'comp']
    subject_ex = 'math'
    result = how_often(subject_log_ex, subject_ex)
    print(result)

    # Write TWO tests for subject_study_hours()

    result = subject_study_hours(['comp', 'math', 'comp'], [1, 3, 2], 'comp')
    print(result)

    result = subject_study_hours(['comp', 'math', 'comp'], [1, 6, 2], 'math')
    print(result)

    # Write TWO tests for most_hours()

    result = most_hours(['comp', 'math', 'comp'], [1, 3, 2])
    print(result)

    result = most_hours(['eng', 'comp', 'phys'], [2, 4, 1])
    print(result)


main()
