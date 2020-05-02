# B5 - Ask the user to input two numbers. 
# Decide which is the number of highest value and print this out.

number1 = int(input("Please input a number:\n"))
number2 = int(input("Please input another number:\n"))

if number1 > number2:
  print(str(number1) + " has the highest value")
else: 
  print(str(number2) + " has the highest value")