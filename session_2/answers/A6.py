# A6 - Combine the two input statements above and print out the
# message "Hello, <name>, you are currently <age> years old. In
# 15 years time you will be <age_in_15_years_time>"

# Ask the user for input
name = input("What is your name? ")
current_age = int(input("How old are you? "))

# Calculate the age in 15 years time
age_in_15_years_time = current_age + 15

# Print our message
print("Hello, " + name + ", you are currently " + str(current_age) + " years old. In 15 years time you will be " + str(age_in_15_years_time))

# BONUS: This code is VERY tied into showing the age in 15 years time,
# how could we change this to be more generic and simpler to change if
# we wanted the age in different years?
