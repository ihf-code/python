# A5 - Ask the user to enter their age, tell them how old they will be in 15 years time

# Ask for user input, cast into an integer and store in a variable
current_age = int(input("How old are you? "))

# Calculate the age in 15 years time
age_in_15_years_time = current_age + 15

# Print the result - cast the integer back to a string
print("In 15 years time you will be: " + str(age_in_15_years_time))
