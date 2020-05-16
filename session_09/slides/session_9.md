# [fit] IHF: Code
## Python — Session 9

---

# Review

---

# Functions

---

# Functions — Create

```python
def hello_world():
    print("Hello World!")
```

---

# Functions — Call

[.code-highlight: 4]
```python
def hello_world():
    print("Hello World!")

hello_world()
```

---

# Functions — Parameters

```python
def hello(name):
    print("Hello, " + name + "!")

hello("Alice")
hello("Bob")
hello("Charlie")
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

# Functions — Parameters

```python
def area(x, y, z):
    print("The area is " + str(x * y * z))

area(12, 3, 4)
area(6, 14, 10)
```

---

# Functions — Parameters

```python
def <function_name>(<param_1>, <param_2>, ...):
    <your code here>
```

---

# Functions — Returning

```python
def area(x, y, z):
    return x * y * z

cube1 = area(12, 3, 4)
cube2 = area(6, 14, 10)
```

---

# Functions — Single Job

```python
def hello(name, age):
    print("Hello my name is " + name)
    print("I'm " + str(age) + " years old")
    print("In 10 years time I will be " + str(age_in_x_years(age, 10)))

def age_in_x_years(age, years):
    return age + years

hello("Alice", 22)
hello("Bob", 34)
hello("Charlie", 17)
```

---

# Functions — Recursion

```python
def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x - 1))

num = 4
print("The factorial of " + num + " is " + str(calc_factorial(num)))
```

---

# Functions — Recursion

```python
def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x - 1))

# calc_factorial(4)              # 1st call with 4
# 4 * calc_factorial(3)          # 2nd call with 3
# 4 * 3 * calc_factorial(2)      # 3rd call with 2
# 4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
# 4 * 3 * 2 * 1                  # return from 4th call as number=1
# 4 * 3 * 2                      # return from 3rd call
# 4 * 6                          # return from 2nd call
# 24                             # return from 1st call
```

---

# Files

---

# Files — Open
```python
f = open("my_file.txt", "r")
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
```

---

# Files — Write

[.code-highlight: 5-7]
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

# [fit]Questions?

---

# Object Oriented Programming 

---
# Object Oriented Programming 
Before OOP, most programs were a list of instructions that acted on memory in the computer. 
OOP, however, is modeled around objects that interact with each other. 
Python is an OOP language. 

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
```

---

# Object 

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
    
    def get_wheels(self):
		# This wouldn't work as you require self. if pulling the variable from the class
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

# The __init__ function

---
# The __ init __ function

All classes have a built-in function called __init__()
This is always the first function executed when the class is being initiated.

---
# The __ init __ function

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

# Class variables vs instance variables

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

# [fit] Coding Time
## Section A

---

# Questions

# sli.do #ihfcode

---

