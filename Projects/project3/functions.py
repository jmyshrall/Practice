"""
Project Three: Import Random
File: comp424/project3/fizzbuzz.py
Initial author: Mihaela Sabin
Collaborator: Justin Myshrall
"""
import random


def password_8chars(letters, caps, numbers):
    """
    Create an 8-character password with characters randomly selected from
    `letters`, `caps`, and `numbers`.
    :param letters: string of lowercase letters
    :param caps: string of uppercase letters
    :param numbers: string of decimal digit characters
    :return: string of 8 characters
    """
    all_chars = letters + caps + numbers
    new_password = ""
    for _ in range(8):
        char = random.choice(all_chars)
        new_password += char
    return new_password


def password_4words(nouns, verbs, adj):
    """
    Create a password of 3 words, randomly selected from `nouns`, `verbs`,
    and `adj` lists.
    :param nouns: list of noun words
    :param verbs: list of verb words
    :param adj: list of adjective words
    :return: string
    """
    all_words = nouns + verbs + adj
    new_password2 = ""
    for _ in range(3):
        word = random.choice(all_words)
        new_password2 += word
    return new_password2


def password_4words_better(nouns, verbs, adj):
    """
    Call password_4words() to create the password and then replace some
    letters as follows:
        - 'o' is replaced with '0'
        - 'l' is replaced  '!'
        - 'a' is replaced with '@'
        - 'e' is replaced with '3'
    :param nouns: list of noun words
    :param verbs: list of verb words
    :param adj: list of adjective words
    :return: string
    """

    all_words = nouns + verbs + adj
    new_password3 = ""
    for _ in range(3):
        word = random.choice(all_words)
        new_password3 += word

    return new_password3


def main():
    """
    Test the functions defined in this module.
    """
    # Write 2 tests for password_8chars()
    letters = "abcdefg"
    caps = "ABCDEFG"
    numbers = "123456"
    my_password = password_8chars(letters, caps, numbers)
    print(my_password)

    # Write 2 tests for password_4words()
    nouns = ["car", "tree", "bag"]
    verbs = ["run", "jump", "dance"]
    adj = ["tall", "short", "long"]
    my_password2 = password_4words(nouns, verbs, adj)
    print(my_password2)

    # Write 2 tests for password_4words_better()
    nouns = ["car", "tree", "bag"]
    verbs = ["ran", "move", "dance"]
    adj = ["tall", "short", "long"]
    my_password3 = password_4words(nouns, verbs, adj)
    my_password3 = my_password3.replace('o', '0')
    my_password3 = my_password3.replace('l', '!')
    my_password3 = my_password3.replace('a', '@')
    my_password3 = my_password3.replace('e', '3')
    print(my_password3)


main()
