"""
Learn and practice histogram pattern
File: comp424/project4/histograms_and_dictionaries
.py
Initial author: Mihaela
Developer: Justin Myshrall
Date: 3/23/2023
"""


def sessions_by_subject(study_log):
    """
    Find out how many study sessions each subject in the `subject_log` has.
    The study log is kept ongoing during the semester to record the study
    sessions associated with various subjects. Thus, a subject appears multiple
    times in the `study_log`.
    :param study_log: list of strings, representing subjects,
        e.g., ['comp', 'math', 'eng', 'comp', 'math', 'comp']
    :return: dictionary, representing how many times each subject is found in
    the `study_log`.
        key: str, representing a unique subject
        values: positive integer, representing frequency of subject
    Example: session_by_subject(['comp, 'math', 'eng', 'comp', 'math', 'comp')
        returns {'comp': 3, 'math': 2, 'eng': 1}
    """

    tally = {}
    for subject in study_log:
        if subject in tally:
            tally[subject] += 1
        else:
            tally[subject] = 1
    return tally


def session_total(study_log_d):
    """
    Calculate the total number of sessions for all subjects in the study_log_d`.
    :param study_log_d: dictionary, representing how many study sessions are
    associated with each subject
        key: str, representing a unique subject
        values: positive integer, representing number of hours
    :return: positive integer
    Example: session_total({'comp': 3, 'math': 2, 'eng': 1})
        returns 6
    """
    total_sessions = 0
    for sessions in study_log_d.values():
        total_sessions += sessions
    return total_sessions


def most_studied(study_log_d):
    """
    Find the subject or subjects with the most study sessions.
    :param study_log_d: dictionary, representing how many study sessions are
    associated with each subject
        key: str, representing a unique subject
        values: positive integer, representing number of hours
    :return: list of the most studied sessions
    Example: most_study({'comp': 3, 'math': 2, 'eng': 3})
        returns ['comp', 'eng']
    """
    max_sessions = 0
    most_studied_subjects = []
    for subject, sessions in study_log_d.items():
        if sessions > max_sessions:
            max_sessions = sessions
            most_studied_subjects = [subject]
        elif sessions == max_sessions:
            most_studied_subjects.append(subject)
    return most_studied_subjects


def subjects_by_session_numbers(study_log_d):
    """
    Find the subjects associated with each unique number of study sessions.
    :param study_log_d: dictionary, representing how many study sessions are
    associated with each subject
        key: str, representing a unique subject
        values: positive integer, representing number of hours
    :return: dictionary
        keys: number of sessions
        values: lists of strings representing subjects
    Example: subject_by_number_of_sessions({'comp': 3, 'math': 2, 'eng': 3}
        returns {3: ['comp', 'eng'], 2: ['math']}
    """
    result = {}

    for subject, sessions in study_log_d.items():
        if sessions in result:
            result[sessions].append(subject)
        else:
            result[sessions] = [subject]

    return result


def main():
    """
    Test the functions defined in this module.
    """
    # Write TWO tests for session_by_subject()
    study_log = ['comp', 'math', 'eng', 'comp', 'math', 'comp']
    expected = {'comp': 3, 'math': 2, 'eng': 1}
    actual = sessions_by_subject(study_log)
    print(f'expected is {expected}')
    print(f'actual is {actual}')

    study_log = ['comp', 'comp', 'eng', 'comp', 'math', 'comp', 'math']
    expected = {'comp': 4, 'math': 2, 'eng': 1}
    actual = sessions_by_subject(study_log)
    print(f'expected is {expected}')
    print(f'actual is {actual}')

    # Write TWO tests for session_total()
    study_log_d = {'comp': 3, 'math': 2, 'eng': 1}
    actual = session_total(study_log_d)
    expected = 6
    print(f'expected is {expected}')
    print(f'actual is {actual}')

    study_log_d = {'comp': 7, 'math': 2, 'eng': 4}
    actual = session_total(study_log_d)
    expected = 13
    print(f'expected is {expected}')
    print(f'actual is {actual}')

    # Write TWO tests for most_studied()
    study_log = {'comp': 3, 'math': 2, 'eng': 3}
    actual = most_studied(study_log)
    expected = ['comp', 'eng']
    print(f"The expected most studied subject are: {expected}")
    print(f"The actual most studied subjects are: {actual}")

    study_log = {'comp': 1, 'math': 2, 'eng': 1}
    actual = most_studied(study_log)
    expected = ['math']
    print(f"The expected most studied subject are: {expected}")
    print(f"The actual most studied subjects are: {actual}")

    # Write TWO tests for subject_by_session_number()
    study_log_d = {'comp': 3, 'math': 2, 'eng': 3}
    expected = {3: ['comp', 'eng'], 2: ['math']}
    actual = subjects_by_session_numbers(study_log_d)
    print(f'The expected subject by session number is: {expected}')
    print(f'The actual subject by session number is: {actual}')

    study_log_d = {'comp': 4, 'math': 1, 'eng': 4}
    expected = {4: ['comp', 'eng'], 1: ['math']}
    actual = subjects_by_session_numbers(study_log_d)
    print(f'The expected subject by session number is: {expected}')
    print(f'The actual subject by session number is: {actual}')


main()
