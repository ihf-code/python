# A4 - Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
# If they get it wrong, print "Password failure" and then ask them to enter it again.
# Only allow them to enter the password wrong 3 times before printing "System Locked!"

# user_input will let your user input their password
# the password variable is hardcoded so you can see if it matches with your user_input
user_input = input("What is your password?\n")
password = "qwerty123"

# if the user input matches the password, it will state you have successfully logged in
# else it will print password failure and a#sk for another input.
# user guesses will count the amount of times you attempty a password
# after 3 guesses (remember Python starts at 0), the loop will end and System Failure will be printed.
user_guesses = 0

while user_guesses < 2:
    if user_input == password:
        print("You have successfully logged in.")
        break
    else:
        print("PASSWORD FAILURE\n")
        user_input = input("What is your password?\n")
        user_guesses += 1
print("System Failure")
