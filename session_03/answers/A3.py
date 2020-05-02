# A3 - Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
# If they get it wrong, print "Password failure"

password = "qwerty123"
user_guess = input("What is your password?\n")

if user_guess == password:
    print("You have successfully logged in.")
else:
    print("Password failure.")
