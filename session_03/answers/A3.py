# A3 - Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
# If they get it wrong, print "Password failure"

# Created variable name and assigned the input to it. 
# Whatever the user enters as their password will be stored in the user_guess variable.
user_guess = input("What is your password?\n")
# Hardcoded password variable so we can compare this against the user_guess
password = "qwerty123"

# Checking if the password is the same as the user_guess. 
# If it is the same, print "You have successfully logged in."
if user_guess == password:
    print("You have successfully logged in.")
# If it is not the same, print "Password failure."
else:
    print("Password failure.")
