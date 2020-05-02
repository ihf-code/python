# A8 - Take a whole number input, 
# if it's positive, print out the number cubed, 
# if it is a negative, print out half its value.

number = int(input("Pick a number:\n"))
if number >=0:
  print(number**3)
else:
  print(number/2)