# B3
# i   - Ask the user to enter the name of a month. If the user enters March/April/May: print " is in Spring", otherwise print "I don't know"
# ii  - Expand for the rest of the year, given that summer is June/July/August.
# iii - Autumn is September/October/November. Winter is December/January/February
# iv  - Ensure that when an unknown month is given it prints "I don't know"

month = input("Pick a month:\n")

if month == "March" or month == "April" or month == "May":
    print(month + " is in Spring")
elif month == "June" or month == "July" or month == "August":
    print(month + " is in Summer")
elif month == "September" or month == "October" or month == "November":
    print(month + " is in Autumn")
elif month == "December" or month == "January" or month == "February":
    print(month + " is in Winter")
else:
    print("I don't know")
