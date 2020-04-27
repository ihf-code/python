# B6 - Your company has had a fantastic year and are now going to offer 
# a bonus of 20% to any employee who has a service of over 7 years, 
# a bonus of 15% to any employee who has a service of over 5 years 
# and a bonus of 10% to any employee who has a service of 3 - 5 years. 
# Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

salary = int(input("What is your current salary?\n"))
years_of_service = int(input("How many years have you worked here?\n"))

if years_of_service > 7:
  print("Your current salary is " + str(salary)+ ", your bonus is " + str(salary*0.2))
elif years_of_service > 5:
  print("Your current salary is " + str(salary)+ ", your bonus is " + str(salary*0.15))
elif years_of_service >= 3 and years_of_service <= 5:
  print("Your current salary is " + str(salary)+ ", your bonus is " + str(salary*0.1))
else:
  print("Your current salary is " + str(salary)+ ", you get no bonus.")