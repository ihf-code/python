# B4 - Ask the user for two different numbers, if both numbers are even, 
# print "Even", if both numbers are odd, print "Odd", 
# else print the product of the two numbers

number_1 = int(input("Input a number:\n"))
number_2 = int(input("Input another number:\n"))

if (number_1 % 2 == 0 and number_2 % 2 == 0):
    print("Both numbers are even.")
elif (number_1 % 2 == 1 and number_2 % 2 == 1):
    print("Both numbers are odd.")
else:
    print(number_1 * number_2)
