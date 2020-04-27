# 11. Print out the sentence from A10 but make the month upper case.

# Ask the user for input for the month and the temperatures
month = input("What month is it?\n")
temp1 = int(input("What was the temperature on Monday?\n"))
temp2 = int(input("What was the temperature on Tuesday?\n"))
temp3 = int(input("What was the temperature on Wednesday?\n"))
temp4 = int(input("What was the temperature on Thursday?\n"))
temp5 = int(input("What was the temperature on Friday ?\n"))

# Work out the average by adding all the temperatures and dividing by the number of temperatures
average_temp = (temp1 + temp2 + temp3 + temp4 + temp5)/5

# Print out the whole string, not forgetting to cast the integer values to strings, this time add .upper() to month
print("It is " + month.upper() + " and the average temperature is " + str(average_temp) + " degrees celsius.")