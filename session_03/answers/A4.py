# A4 - Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd"

# Created variable number and assigned the input to it.
# As we will be performing some math on this input, we will need to cast it to an integer.
# Whatever the user enters as their number will be stored in the number variable.
number = int(input("Please enter a number to find out if it is even or odd:\n"))

# Checking if the number is even, we do this by using the modulus to check if when divided by 2 the remainder is 0 
# If it is the same, print(str(number) + " is Even") - as number is an integer, to concatenate, we have to cast to a string.
if number % 2 == 0:
    print(str(number) + " is Even")
# If it is not even, it must be odd so will print(str(number) + " is Odd"), again casting the number to a string.
else:
    print(str(number) + " is Odd")
