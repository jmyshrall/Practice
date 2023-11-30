"""
Solve Parsons Problems and computational problems to learn how to:
- document, test, design, implement, and debug functions.
File: comp424/homework1/fizzbuzz.py
Initial author: Mihaela
Contributor: Justin Myshrall
Collaborator(s):
"""


def ch2_sec17_ex13():
    """
    Write the statements given in Ch 2, Sec 13, Exercise 13 in the order
    that implements the following function:
    A user is asked for two numbers, and then the sum of those numbers.
    """
    num_one = input("Please enter your first number")
    num_two = input("Please enter your second number")
    sum_of_input = int(num_one) + int(num_two)
    print(sum_of_input)


def ch6_sec10_ex2():
    """
    Write the statements given in Ch 6, Sec 10, Exercise 2 in the order that
    implements the following function:
    Determine how mamny t's in the list `phrases`.
    """
    phrases = ["My, what a lovely day it is!", "Have you mastered cooking yet? A tasty treat could be in your future.",
               "Have you seen the leaves change color?"]
    for sentences in phrases:
        print(sentences.count("t"))


def ch7_sec6_activity_7_6_7():
    """
    Write the statements given in Ch 7, Sec 6, Activity 7.6.7 (pp6_6_1) in the
    order that implements the following function:
    Add up the first `n` numbers when `n` is provided by the user.
    """
    n = int(input('How many odd numbers would you like to add together?'))
    thesum = 0
    oddnumber = 1
    for counter in range(n):
        thesum = thesum + oddnumber
        oddnumber = oddnumber + 2
    print(thesum)


def count_odd(lst):
    """
    Count how many odd numbers are in the `num_list`.
    :param lst: list of integers
    :return: integer
    Examples:
        count_odd([2, 3, 4, 5]) returns 2
        count_odd([2, 4]) returns 0
        count_add([]) returns 0
    This is Ch 12, Sec 17, exercise 10.
    """
    count = 0
    for num in lst:
        if num % 2 != 0:
            count += 1
    return count


my_list = [1, 2, 3, 4, 5]
num_odd = count_odd(my_list)
print("Number of odd integers in the list:", num_odd)

# ch2_sec17_ex13()

# ch6_sec10_ex2()

# ch7_sec6_activity_7_6_7()

# count_odd(lst)


def main():
    """
    Test the functions defined in this module.
    """

    main()
