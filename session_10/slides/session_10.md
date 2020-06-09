# [fit] IHF: Code
## Python — Session 10

---

# Review

---

# Variables

```python
name = "Charlie"
age = 27
left_to_pay = 29.99
has_paid = False
```

---

# Numerical Operators

```python
x = 3
y = 6

print(1 + 2)
print(y - x)

area = x * y
print(area)

squared = x ** 2
```

---

# Concatenation

```python
first_name = "Bob"
last_name = "Jones"
full_name = first_name + " " + last_name

print("Hello " + first_name)
print("Good morning, " + full_name)
```

---

# Casting

```python
x = int(8.3)  # x will be 8
y = float(9)  # y will be 9.0
z = str(10.0) # z will be '10.0'
```

---

# Input

```python
name = input("What's your name? ")
print("Hello " + name)

age = int(input("How old are you? "))
age_in_10_years = age + 10
print("In 10 years you will be " + str(age_in_10_years))
```

---

# If

```python
age = int(input("How old are you? "))
if age >= 18:
    print("You can vote!")
```

---

# If / Else

```python
age = int(input("How old are you? "))
if age >= 18:
    print("You can vote!")
else:
    print("Try voting next time")
```

---

# If / Else / Elif

```python
name = "Bob"
if name == "Alice":
    print("Hello Alice")
elif name == "Bob":
    print("Hello Bob")
else:
    print("You must be Charlie")
```

---

# For Loops

```python
names = ["Alice", "Bob", "Charlie"]

for person in names:
    print(person)

# Alice
# Bob
# Charlie
```

---

# For Loops

```python
for letter in "supercalifragilisticexpialidocious":
    print(letter.upper())
```

---

# While Loops

```python
guess = None
while guess != 4:
    # Continues to ask for a number until you enter 4
    guess = int(input("What's your number? "))
```

---

# While Vs For Loop

```python
x = 1
while x <= 100:
    print(x)
    x += 1

for y in range(1, 101):
    print(y)
```

---

# Collections — List

```python
names = ["Alice", "Bob", "Charlie"]

names.append("Dave") # ["Alice", "Bob", "Charlie", "Dave"]

names[2] = "Chris" # ["Alice", "Bob", "Chris", "Dave"]

del(names[1])# ["Alice", "Chris", "Dave"]

if "Eve" in names:
    print("Eve is here")

for name in names:
    print(name)
```

---

# Collections — Tuple

```python
colours = ("Red", "Blue", "Green")
print(colours[0]) # Red
print(colours[1]) # Blue
print(colours[2]) # Green
```

---

# Collections — Set

```python
fruit = {"Apple", "Banana", "Cherry"}
for item in fruit:
    print(item)
```

---

# Collections — Dictionary

```python
shirt = {
    "size": "Large",
    "colour": "Red"
}

print(shirt["size"]) # Large

shirt["material"] = "Cotton" # Add new key/value pair
shirt["colour"] = "Green" # Change existing value

del(shirt["size"]) # Delete key/value pair

if "material" in shirt:
    print("The material is: " + shirt["material"])

for key in shirt:
    print(str(key) + " = " + str(shirt[key]))
```

---

# Nested Collections

```python
phone_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]

for row in phone_grid:
    for column in row:
        print(column)
```

---

# List of Dictionaries

```python
contacts = [
    {"fname": "Alice", "lname": "Smith"},
    {"fname": "Bob", "lname": "Jones", "phone": "555-1234"},
    {"fname": "Charlie", "lname": "McCloud"}
]

for person in contacts:
    if "phone" in person:
        print(person["fname"])
```

---

# Functions

```python
def hello_world():
    print("Hello World!")


hello_world()
```

---

# Functions — Parameters

```python
def hello(name, age):
    print("Hello my name is " + name)
    print("I'm " + str(age) + " years old")

    age_in_10_years = age + 10
    print("In 10 years time I will be " + str(age_in_10_years))


hello("Alice", 22)
hello("Bob", 34)
hello("Charlie", 17)
```

---

# Default Arguments

```python
def hello(name = "World"):
    print("Hello " + name)


hello("Jake")
hello("Saf")
hello() # Hello World
```

---

# Keyword Arguments

```python
def add_result(player_1, player_1_score):
    # ...
    # Process the data passed in
    # ...

# Allows you to pass arguments in any order
add_result(player_1 = "Jake", player_1_score = 8)
add_result(player_1_score = 8, player_1 = "Jake")
```

---

# Functions — Returning

```python
def volume(x, y, z):
    return x * y * z


cube1 = volume(12, 3, 4)
cube2 = volume(6, 14, 10)
```

---

# Returning multiple variables

```python
def my_func():
    return 10, 20, 30


x, y, z = my_func()

# x = 10
# y = 20
# z = 30
```

---

# \*args — Arguments

```python
def count_numbers(*args):
    # return sum(args)
    total = 0
    for num in args:
        total += num

    return total

print(count_numbers(1, 3)) # 4
print(count_numbers(1, 3, 5)) # 9
print(count_numbers(1, 3, 5, 7)) # 16
print(count_numbers(1, 3, 5, 7, 9)) # 25
print(count_numbers(1, 3, 5, 7, 9, 11)) # 36
```

---

# \*args — Arguments

```python
from random import randint

def roll(*dice):
    return sum(randint(1, die) for die in dice)
    # count = 0
    # for die in dice:
    #     count += randint(1, die)
    # return count

roll(20) # 1–20
roll(6, 6) # 1–12
roll(6, 6, 6) # 1–18
```

---

# \*\*kwargs — Keyword Arguments

```python
def my_func(**kwargs):
    print(kwargs)

my_func(name = "Jake", location = "Manchester")
# {'name': 'Jake', 'location': 'Manchester'}
```

---

# \*args & \*\*kwargs

```python
def add_item(*args, **kwargs):
    print(args)
    print(kwargs)


add_item(
    "18971", # internal ID
    "A guide to Python", # Item Name
    "book", # Item Type
    author = "Alice Smith",
    isbn = "1234567890123"
)

# ('18971', 'A guide to Python', 'book')
# {'author': 'Alice Smith', 'isbn': '1234567890123'}
```

---

# Files — Read

```python
f = open("my_file.txt", "r")
print(f.read())
```

---

# Files — Read

```python
f = open("my_file.txt", "r")
for x in f:
  print(x)
```

---

# Files — Handling

| Value |  Action | Description |
|--- | --- | --- |
| "r" | Read | Opens a file for reading, error if the file does not exist
| "a" | Append | Opens a file for appending, creates the file if it does not exist
| "w" | Write | Opens a file for writing, creates the file if it does not exist
| "x" | Create | Creates the specified file, returns an error if the file exists

---

# Files — Write

```python
f = open("example.txt", "w")
f.write("Hello World")
f.close()

f = open("example.txt", "a")
f.write("It's nice to be here")
f.close()
```

---

# Files — Write

```python
f = open("names.txt", "a")

name = True
while name:
    name = input("Enter a name: ")
    f.write(name + "\n")

f.close()
```

---

## Any Questions?
### sli.do #ihfcode

---

# What is Object Oriented Programming?

---
# Object Oriented Programming
Before OOP, most programs were a list of instructions that acted on memory in the computer.
OOP, however, is modeled around objects that interact with each other.
Python is an OOP language.

---

# Why do we use Object Oriented Programming?
Encapsulate the data with the code that manipulates that data.

---

# Class

---
# Class
A class is the blueprint for an object.

---

# Class

```python
class Name_of_your_class:
    <your code here>
```

---

# Class

```python
class Car:
	wheels = 4

    def drive():
        #code that makes the car drive
```

---

# Object
```python
class Car:
	wheels = 4


volvo = Car()
```

---

# Object
An object, is an instance of that class.
It uses the blueprint of class to create its own object.

---

# To instantiate an object
Instantiating an object is creating an object from the class.

```python
class Car:
	wheels = 4


volvo = Car()
```

---

# Object

```python
class Car:
	wheels = 4


volvo = Car()
print(volvo.wheels)
```

---

# The self parameter

---
# The self parameter
The self parameter allows you to pass variables from the class when instantiating the object

---
# The self parameter

```python
class Car:
	wheels = 4

    def get_wheels(self.wheels):
		# This wouldn't work as you require 'self.'
        # if you are pulling the variable from the class
        print(wheels)

```

---

# The self parameter

```python
class Car:
	wheels = 4

    def get_wheels(self):
        print(self.wheels)

```

---

# The self parameter

```python
class Car:
	wheels = 4

    def get_wheels(self):
        print(self.wheels)


mercedes = Car()
mercedes.get_wheels()

```
---

# [fit]The \_\_init\_\_ function

---

# The \_\_init\_\_ function

All classes have a built-in function called \_\_init\_\_()
This is always the first function executed when the class is being initiated into an object.

---
# The \_\_init\_\_ function

```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour
    self.miles = miles


volvo = Car("red", 30000)

print(volvo.colour)
print(volvo.miles)
```

---

# Object Methods

---

# Object Methods
Methods in objects are functions that belong to the object.

---

# Object Methods

```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour
    self.miles = miles

  #This is the object method
  def car_information(self):
    print("This car is " + self.colour + " and has " + str(self.miles) + " miles.")


volvo = Car("red", 30000)

print(volvo.colour)
print(volvo.miles)
volvo.car_information()
```

---

# Modify Object Properties

```python
volvo = Car("red", 30000)
print(volvo.colour) #red

volvo.colour = “blue”
print(volvo.colour) #blue
```

---

# Delete Object Properties

```python
volvo = Car("red", 30000)

print(volvo.miles) #30000

del volvo.miles

print(volvo.miles) #AttributeError: 'Car' object has no attribute 'miles'
```

---

# The pass statement

---

# The pass statement
If have a class definition with no content, put in the pass statement to avoid getting an error.

---

# The pass statement
```python
class Car:
    pass
```

---

# Inheritance

---

# Parent Class

---

# Parent Class

The parent class is the class being inherited from.
Any class can be a parent class, so the syntax is the same as creating any other class.

---

# Parent Class

```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour
    self.miles = miles

  def car_information(self):
    print("This car is " + self.colour + " and has " + str(self.miles) + " miles.")


volvo.car_information() # This car is red and has 30000 miles.
```

---

# Child Class

---

# Child Class

Child class is the class that inherits from another class
To create a child class, you pass the parent class as a parameter.

---

# Child Class
```python
class Volvo(Car):
    pass      
```

---

# Child Class

The child class (Volvo) has the same methods and properties as the parent class (Car).

---

# Child Class

```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour
    self.miles = miles

  def car_information(self):
    print("This car is " + self.colour + " and has " + str(self.miles) + " miles.")


class Volvo(Car):
  pass


volvo_s90 = Volvo("black", 20000)
volvo_s90.car_information() # This car is black and has 20000 miles.
```

---

# The \_\_init\_\_ function

When you add the \_\_init\_\_ function to the child class, it no longer inherits the parents.

---

# The \_\_init\_\_ function

```python
class Volvo(Car):
  def __init__(self, colour, miles):
```

---

# The \_\_init\_\_ function

To keep the parent's \_\_init\_\_ function, add a call to the parent's \_\_init\_\_ function.

---

# The \_\_init\_\_ function

```python
class Volvo(Car):
  def __init__(self, colour, miles):
    Car.__init__(self, colour, miles):
```

---

# The super() function

The super function will make the child class inherit all the methods and properties from its parent.

---

# The super() function

```python
class Volvo(Car):
  def __init__(self, colour, miles, seats):
    super().__init__(colour, miles)
```

---

# Adding properties to the child class

```python
class Volvo(Car):
  def __init__(self, colour, miles, seats):
    super().__init__(colour, miles)

    #Adding another property to the child class
    self.seats = seats


volvo_s90 = Volvo("black", 20000, 5)
print(volvo_s90.seats)
```

---

# Adding methods to the child class

```python
class Volvo(Car):
  def __init__(self, colour, miles, seats):
    super().__init__(colour, miles)
    self.seats = seats

  #Adding another method to the child class
  def more_car_info(self):
    print("This car is " + self.colour + ", has " + str(self.miles) +
    " miles and " + str(self.seats) + " seats.")


volvo_s90 = Volvo("black", 20000, 5)
volvo_s90.more_car_info()
```

---

# [fit] Coding Time
## Section A

---

### Questions?
### go to sli.do #ihfcode

---

# [fit] Next Session
### Thursday 11th June 2pm
### Answers
