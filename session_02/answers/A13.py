# 13. Ask the user to enter their name as well as a number. 
# Print out the uppercase character at that position in the string.

# Ask the user for input
name = input("What is your name?\n")
number = int(input("Pick a number:\n"))

# Print the number as the index for the name and use .upper()
print(name[number].upper())