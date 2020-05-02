# A school has following rules for their grading system:
# a. Above 80 – A
# b. 60 to 80 – B
# c. 50 to 60 – C
# d. 45 to 50 – D
# e. 25 to 45 – E
# f. Below 25 - F
# Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson1 = input("Input your lesson:\n")
mark1 = int(input("Input your mark:\n"))
lesson2 = input("Input your lesson:\n")
mark2 = int(input("Input your mark:\n"))
lesson3 = input("Input your lesson:\n")
mark3 = int(input("Input your mark:\n"))

print("REPORT CARD:")

#Lesson 1
if mark1 > 80:
  print(lesson1 + " - A grade")
elif mark1 <= 80 and mark1 > 60:
  print(lesson1 + " - B grade")
elif mark1 <= 60 and mark1 > 50:
  print(lesson1 + " - C grade")
elif mark1 <= 50 and mark1 > 45:
  print(lesson1 + " - D grade")
elif mark1 <= 45 and mark1 > 25:
  print(lesson1 + " - E grade")
elif mark1 < 25:
  print(lesson1 + " - F grade")
else:
  print("Go to see your teacher")

#Lesson 2
if mark2 > 80:
  print(lesson2 + " - A grade")
elif mark2 <= 80 and mark2 > 60:
  print(lesson2 + " - B grade")
elif mark2 <= 60 and mark2 > 50:
  print(lesson2 + " - C grade")
elif mark2 <= 50 and mark2 > 45:
  print(lesson2 + " - D grade")
elif mark2 <= 45 and mark2 > 25:
  print(lesson2 + " - E grade")
elif mark2 < 25:
  print(lesson2 + " - F grade")
else:
  print("Go to see your teacher")

#Lesson 3
if mark3 > 80:
  print(lesson3 + " - A grade")
elif mark3 <= 80 and mark3 > 60:
  print(lesson3 + " - B grade")
elif mark3 <= 60 and mark3 > 50:
  print(lesson3 + " - C grade")
elif mark3 <= 50 and mark3 > 45:
  print(lesson3 + " - D grade")
elif mark3 <= 45 and mark3 > 25:
  print(lesson3 + " - E grade")
elif mark3 < 25:
  print(lesson3 + " - F grade")
else:
  print("Go to see your teacher")