"""
Parsons Problems: Flow of execution, functions, iteration.
File: comp424/project2/fizzbuzz.py
Initial author: Mihaela Sabin
Collaborator: Justin Myshrall
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


def ch6_sec10_ex1():
    """
    Write the statements given in Ch 6, Sec 10, Exercise 1 in the order that
    implements the following function:
    Print out the length of each item in the list`weather` as well as the
    first and the last characters of the item.
    """
    weather = ["sunny", "cloudy", "partially sunny", "rainy", "storming", "windy", "foggy", "snowy", "hailing"]
    for condition in weather:
        print("the word is", len(condition), "characters")
        first_char = condition[0]
        last_char = condition[-1]
        print("the first character is: " + first_char)
        print("the last character is: " + last_char)


def ch7_sec14_ex11():
    """
    Write the statements in Ch 7, Sec 14, Exercise 11 in the order that
    implements the following function:
    1) Print out a greeting to each student in the list`num_students`, and
    2) Print out how many students have entered the room at the time the
    greeting happened.
    """
    students = ["Jay", "Stacy", "Iman", "Trisha", "Ahmed", "Daniel", "Shadae", "Tosin", "Charlotte"]
    num_students = 0
    for students in students:
        print("welcome to class, " + students)
        num_students += 1
        print(str(num_students) + "student(s) have entered the classroom")


def sum_of_squares(number_list):
    """
    Compute the sum of squares of the numbers in the list `num_list`.
    :param number_list: list of integers
    :return: integer
    Example: sum_of_squares([2, 3, 4]) returns 4+8+16, which s 29.
    This is Ch 12, Sec 17, Exercise 9.
    """
    answer = 0
    for num in number_list:
        answer = answer + (num * num)
    return answer


num_list = [2, 3, 4]
result = sum_of_squares(num_list)
print(result)


# ch2_sec17_ex13()

# ch6_sec10_ex1()

# ch7_sec14_ex11()

# sum_of_squares(num_list)


def main():
    """
    Test the functions defined in this module.
    """


main()
