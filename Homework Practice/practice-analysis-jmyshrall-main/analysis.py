"""
Learning goals:
- More practice with reading from and writing to files.
- More practice with processing collections.
File: comp424/practice-analysis/analysis.py
Initial author: Mihaela
Developer: Justin Myshrall
Collaborator: None
Date: 4/20/2023
"""


def read_data(filename):
    """
    Read data from text file named `filename`. The file has lines of
    comma-separated strings, such that:
    - 1st string has info about a loan
    - 2nd string has info about the name of the country that got the loan
    - 3rd string has info about the time it took to raise the loan
    - 4th string has info about the number of lenders who contributed to the
        loan
    :param filename: string
    :return: list of dictionaries, each dictionary has 4 key-value pairs
        keys: 'loan', 'country', 'raising_time', 'lenders'
        values: strings, such that 1st string corresponds to 'loan' key,
            2nd string to 'country' key, 3rd to `raising_time` key, and
            4th string to 'lenders' key
    Example: For the file named 'data_1.csv', the function returns a list
    with a single dictionary:
    [{'loan':1250.0, 'country': 'Azerbaijan', 'raising_time':193075,
        'lenders':31}]
    """
    with open(filename, encoding='utf-8') as f_in:
        lines_list = f_in.readlines()
    d_list = []
    for line in lines_list:
        line = line.rstrip('/n')
        values_list = line.split(',')
        line_d = {}
        line_d['loan'] = float(values_list[0])
        line_d['country'] = values_list[1]
        line_d['raising_time'] = int(values_list[2])
        line_d['lenders'] = int(values_list[3])
        d_list.append(line_d)
    return d_list

def total_loan_amount(d_list):
    """
    Calculate the total amount of loans by summing up the values corresponding
    to the 'loan' key in `data_d` dictionary    :param d_list:
    :return: float, total amount of loans
    Example: if the dictionary is {'loan':1250.0, 'country': 'Azerbaijan',
        'raising_time':193075, 'lenders':31}
    the function returns 1250.0
    """


def avg_lenders_per_loan(d_list):
    """
    Calculate the average number of lenders who contributed to a loan.
    :param d_list: dictionary
    :return: integer, average number
    """


def smallest_loan_country(d_list):
    """
    Find the country in `country_names` that received the smallest loan.
    :param d_list: dictionary
    :return: string, name of the country with the smallest loan
    """


def time_per_dollar_raised(d_list):
    """
    Find the time per dollar raised for each loan by dividing the loan amount
    value by the raising time value for each loan.
    :param d_list: dictionary
    :return: list of floats
    """
