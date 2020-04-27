# B1
# i   - Ask for the user's name, if they are called "Alice" print "Hello, Alice",
# ii  - if they are called "Bob", print "You're not Bob! I'm Bob",
# iii - else print "You must be Charlie"

name = input("What is your name?\n")

if name == "Alice":
    print("Hello, Alice!")
elif name == "Bob":
    print("You're not Bob! I'm Bob..")
else:
    print("You must be Charlie!")
