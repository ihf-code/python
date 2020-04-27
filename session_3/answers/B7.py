# B7 - Take the age and name of three people and determine who is the oldest and youngest 
# and print out the name and age of the oldest and youngest. 
# If all three ages are the same, print that.

name1 = input("What is your name?\n")
age1 = int(input("How old are you?\n"))
name2 = input("What is your name?\n")
age2 = int(input("How old are you?\n"))
name3 = input("What is your name?\n")
age3 = int(input("How old are you?\n"))

#Oldest 
if age1 > age2 and age1 > age3:
  print(name1 + "is the oldest and is " + str(age1) + "years old.")
elif age2 > age1 and age2 > age3:
  print(name2 + "is the oldest and is " + str(age2) + "years old.")
elif age3 > age1 and age3> age2: 
  print(name3 + "is the oldest and is " + str(age3) + "years old.")
else: 
  ("You are all the same age")

#Youngest
if age1 < age2 and age1 < age3:
  print(name1 + "is the youngest and is " + str(age1) + "years old.")
elif age2 < age1 and age2 < age3:
  print(name2 + "is the youngest and is " + str(age2) + "years old.")
elif age3 < age1 and age3 < age2: 
  print(name3 + "is the youngest and is " + str(age3) + "years old.")
else: 
  ("You are all the same age")