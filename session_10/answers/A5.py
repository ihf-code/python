# 5. Create a class called Upper which has two methods called get_word and print_word.
#  - the get_word method should accept a string from the user
#  - the print_word method prints the string in upper case.

class Upper:
    def __init__(self):
        self.word = ""

    def get_word(self):
        self.word = input("Input a word:\n")

    def print_word(self):
        print(self.word.upper())


word1 = Upper()
word1.get_word()
word1.print_word()
