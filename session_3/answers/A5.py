# A5 - Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

number_1 = int(input("Input a number:\n"))
number_2 = int(input("Input another number:\n"))

if number_1 + number_2 > 21:
    print("Bust.")
else:
    print("Safe.")
