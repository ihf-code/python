# A2 - i. Keep asking the user to enter a number until they enter the number 7, then print "Wow! Lucky number 7!
# A2 - ii. Rewrite so that the number being guessed is a random value from 1 to 10

# i
# guess variable stored with a None value, this means it has no value.
import random
guess = None
# the user will input a number, whilst the user number does not equal 7 it will keep asking for a number.
# when the user number equals 7 then it will print "Wow! Lucky number 7!"
while guess != 7:
    guess = int(input("Guess the computer's number:\n"))
print("Wow! Lucky number 7!")

# ii
# as above, but changed guess to a random number between 1 - 10 instead of the user inputting a number.
guess = None
while guess != 7:
    guess = random.randint(1, 10)
    print(guess)
print("Wow! Lucky number 7!")

# iii
# this has now been refactored to be a guessing game between the user and computer.
# the computer picks a random number between 1-10, the user has to try and guess the answer.
# it will keep asking until the user matches.
computer_choice = random.randint(1, 10)
user_choice = 0
while computer_choice != user_choice:
    user_choice = int(input("Guess the computer's number:\n"))
print("Well done! You guess the computer's number!")
