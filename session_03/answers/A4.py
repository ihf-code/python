# A4 - Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd"

number = int(input("Please enter a number to find out if it is even or odd:\n"))

if number % 2 == 0:
    print(str(number) + " is Even")
else:
    print(str(number) + " is Odd")
