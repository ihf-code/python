# A3 - The area of a rectangle is width multiplied by height.
# Ask the user to enter a width and height in cm, then print the area to the complete square metre.

# import the math module
import math
# two variables that store the width and height that the user will input as an integer.
width = int(input("What is the width of your rectangle:\n"))
height = int(input("What is the height of your rectangle:\n"))

# area_in_cm, is th width multiplied by height.
# area_in_m2 is first divided by 10000 to get from cm to m2 and math.ceil will round it up.
area_in_cm = width * height
area_in_m2 = math.ceil(area_in_cm/10000)
print("Your rectangle is " + str(area_in_m2) + ' metres squared.')
