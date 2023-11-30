"""
Learn and practice with Python classes
File: comp424/practice_classes/genpass.py
Initial author: Mihaela
Developer: Justin Myshrall
Collaborator(s): NONE
Date: 4/6/2023
"""

import random


class GeneratePassword:
    """
    Generate 3 different kinds of password.
    Class attributes:
        letters, caps, numbers: of type str
        nouns, adjectives, verbs: of type list of strings
    Instance attribute: password of type string
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    nouns = ['mihaela', 'james', 'ben', 'philip', 'raunchy']
    adjectives = ['wonderful', 'diligent', 'hard-working', 'persistent',
                  'collaboratives']
    verbs = ['hike', 'drive', 'ski', 'lift', 'fish']

    def __init__(self, password='********'):
        """
        Create object with password instance variable set up to "password"
        """
        # define instance variable `self.password` and initialize it with
        # parameter `password`
        self.password = password

    def simple_pass(self):
        """
        Create an 8-character password composed of random digits, lower-case
        letters, and upper-case letters, from the three class variables
        `letters`, `caps`, and `numbers`. Assign it to instance variable
        `self.password`.
        """
        all_chars = (GeneratePassword.letters +
                     GeneratePassword.caps +
                     GeneratePassword.numbers)
        new_password = ''
        for _ in range(8):
            char = random.choice(all_chars)
            new_password += char
        self.password = new_password

    def word_pass(self):
        """
        Create a password by concatenating random words from the three
        class variable `nouns`, `adjectives`, and `verbs`.
        Asking it to the instance variable `self.password`.
        """
        all_words = (GeneratePassword.nouns +
                     GeneratePassword.verbs +
                     GeneratePassword.adjectives)
        new_password = ''
        for _ in range(3):
            word = random.choice(all_words)
            new_password += word
        self.password = new_password

    def word_pass_better(self):
        """
        Call `self.word_pass()` to get a password by concatenating random
        words from the class variables. Modify the returned value to be
        capitalized and to have digits replacing certain letters
            e.g., 1 replaces l, 0 replaces o, and 3 replaces e
        Assign it to the instance variable `self.password`.
        """
        all_words = (GeneratePassword.nouns +
                     GeneratePassword.verbs +
                     GeneratePassword.adjectives)
        new_password = ''
        for _ in range(3):
            word = random.choice(all_words)
            new_password += word
            new_password = new_password.replace('o', '0')
            new_password = new_password.replace('l', '!')
            new_password = new_password.replace('a', '@')
            new_password = new_password.replace('e', '3')
        self.password = new_password

    def print(self):
        """
        Print out instance variable `self.password`
        """
