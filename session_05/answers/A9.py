# A9 - Rewrite question B8 from Week 3 using a while loop.

lesson = None

print("REPORT CARD:")

while lesson != "":
    lesson = input("Input your lesson:\n")
    mark = int(input("Input your mark:\n"))
    if mark > 80:
        print(lesson + " - A grade")
    elif mark <= 80 and mark > 60:
        print(lesson + " - B grade")
    elif mark <= 60 and mark > 50:
        print(lesson + " - C grade")
    elif mark <= 50 and mark> 45:
        print(lesson + " - D grade")
    elif mark <= 45 and mark > 25:
        print(lesson + " - E grade")
    elif mark < 25:
        print(lesson + " - F grade")
    else:
        print("Go to see your teacher")