"""
Author: Justin Myshrall
Date: 11/9/2023
"""


class Person:
    def __init__(self, name, age):
        """
        Initializes a Person with a given name and age.

        Param:
        - name (str): The name of the person.
        - age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        """
        Compares the age of the current person with another person.

        Param:
        - other_person (Person): Another Person object.
        Return:
        - str: A message indicating who is older.
        - time complexity: O(1)
        """
        if self.age > other_person.age:
            return f"{self.name} is older."
        elif self.age < other_person.age:
            return f"{other_person.name} is older."
        else:
            return "Both persons are of the same age."


# test case
person1 = Person("Alice", 30)
person2 = Person("Bob", 31)

result = person1.compare_age(person2)
print(result)
