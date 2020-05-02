if True:
    print("This is always run")

if False:
    print("This is never run")

if 3 == 1:
    print("Yes")
else:
    print("No")


age = int(input("How old are you? "))
if age <= 13:
    print("You are 13 or younger")
elif age < 18:
    print("You are between 14 and 17")
elif age == 18:
    print("You are 18")
else:
    print("You are 19 or over")


# Ask for the users name and convert it to lowercase
name = input("What's your name? ").lower()
if name == "alice":
    print("Hey Alice!")
elif name == "bob":
    print("Howdy Bob")
else:
    print("You must be Charlie")


age = int(input("How old are you? "))
if age < 1 or age > 120:
    print("Hmmm...are you sure?")
if age > 12 and age < 20:
    print("You are a teenager")
else:
    print("You are not a teenager")

if not (age > 12 and age < 20):
    print("You are not a teenager")
