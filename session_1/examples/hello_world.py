# Simple "Hello World example"
print("Hello, World!")

# Each print command is printed on to a new line
print("Hello")
print("World")

# Print an integer
print(2019)

# Print a float
print(3.14159)

# Print Boolean values
print(True)
print(False)

# All in one command with the escaped new line character
print("Hello\nWorld!")

# Print a formatted shopping List
print("My Shopping List:")
print("\tApples")
print("\tBread")
print("\tMilk")
print("\tEggs")

# Print a formatted receipt
print("Your Receipt:")
print("Item\t#\tPrice")
print("Apples\t4\t£1.99")
print("Bread\t1\t£1.29")
print("Milk\t2\t£0.79")
print("Eggs\t12\t£2.89")
print("\tTOTAL:\t£6.96")

# Concatinating a variable into the string output
name = "Alice"
print("Hello " + name)

# Convert an integer to a string to allow it to be concatinated
age = 21
print("Hi, my name is " + name + " and I'm " + str(age) + "years old!")

# Ask the use for their name and then display it back to them
users_name = input("What is your name? ")
number_of_characters = len(users_name)
second_letter = users_name[1]
print("Hello " + users_name)
print("Your name has " + str(number_of_characters) + " characters.")
print("The second letter of your name is: '" + second_letter + "'")
