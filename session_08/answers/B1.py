# B1 - Ask the user to enter their name and append this to a file called 'register.txt'

file1 = open("register.txt", "a")

name = True
while name != "":
    name = input("What's your name?\n")
    if name:
        file1.write(name + "\n")

file1.close()

file2 = open("register.txt", "r")
for name in file2:
    print(name)
