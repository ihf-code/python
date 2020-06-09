# A2 - Ask for the user's name, if they are not called "Alice", print "You're not Alice!"

# Created variable name and assigned the input to it. 
# Whatever the user enters as their name will be stored in the name variable.
name = input("What is your name?\n")

# Checking if the name the user has input is not Alice. 
# If it is not Alice, print "You're not Alice!"
if name != "Alice":
    print("You're not Alice!")
