# A5 - Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

# Created variable number and assigned the input to it.
# As we will be performing some math on this input, we will need to cast it to an integer.
# Whatever the user enters as their number will be stored in the number_1 variable.
# Repeated the above for number_2
number_1 = int(input("Input a number:\n"))
number_2 = int(input("Input another number:\n"))

# Checking if when both number variables are added together are over 21, print("Bust.")
if number_1 + number_2 > 21:
    print("Bust.")
# if when both number variables are added together are under 21, print("Safe.")
else:
    print("Safe.")
