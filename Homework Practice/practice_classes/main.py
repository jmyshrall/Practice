"""
Make use of the GeneratorPassword methods.
File: comp424/practice_classes/main.py
Initial Author: Mihaela
Developer:
Collaborator(s):
"""
from genpass import GeneratePassword


def main():
    """
    Call all the methods of `GeneratorPassword` class
    """
    # create GeneratePassword initial object and print it out
    genpass_obj = GeneratePassword()
    genpass_obj.print()

    genpass_obj = GeneratePassword('manchester')
    genpass_obj.print()

    # Change object by calling `genpass_obj.simple_pass()` and print out the
    # generated password
    genpass_obj.simple_pass()
    print(f'simple() generates {genpass_obj.password}')

    # Change object by calling `self.word_pass()` and print out the generated
    # password
    genpass_obj.word_pass()
    print(f'word_pass() generates {genpass_obj.password}')

    # Change object by calling `self.word_pass_better()` and print out the
    # generated password
    genpass_obj.word_pass_better()
    print(f'word_pass_better() generates {genpass_obj.password}')


main()
