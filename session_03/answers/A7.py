# A7 - Your company has had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
# Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
# salary = int(input("What is your current salary?\n"))
# years_of_service = int(input("How many years have you worked here?\n"))

if years_of_service > 3:
  print("Your current salary is" + str(salary)+ ", your bonus is" + str(salary*0.1))
else:
  print("Your current salary is" + str(salary)+ ", you get no bonus.")