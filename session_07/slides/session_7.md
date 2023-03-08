# [fit] KPMG: Code
## [fit] Python — Session 7 — Lesson

---

# Review

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

# For Loops

```python
for olympic_years in range(1896, 2020, 4):
    print(olympic_years)

# ...
# 2008
# 2012
# 2016
```

---

# For Loops

```python
times_to_ask = int(input("How many times should I ask? "))

for x in range(times_to_ask):
    print(input("What is your name? "))
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

# While Loops

```python
times_in_loop = 0
while times_in_loop <= 10:
    print("Hello")
    times_in_loop = times_in_loop + 1
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

# Collections

- List
- Tuple
- Set
- Dictionary

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

## Any Questions?

---

# Functions

---

# Functions

```python
# Prints to the screen
print()

# Takes input from the user
input()

# Casts value to a string
str()

# Casts value to an integer
int()

# Gets the length of the string/list etc
len()
```

---

# What are functions?

- Re-usable, self-contained blocks of code that do a single task

---

# Why do we use functions?

- Lets you re-use code
- Break large problems into smaller ones

---

# Functions — Create

```python
def hello_world():
    print("Hello World!")
```

---

# Functions — Create

```python
def <function_name>():
    <your code here>
```

---

# Functions — Call

```python
def hello_world():
    print("Hello World!")

hello_world()
```

---

# Functions — Call

```python
print("Program starting...")

# This function is never called, and so never runs
def hello_world():
    print("Hello World!")

print("Program ending...")
```

---

# Don't Repeat Yourself (DRY)

```python
print("Hello Alice!")
print("Hello Bob!")
print("Hello Charlie!")
```

---

# Don't Repeat Yourself (DRY)

```python
# We have changed the message 3 times
print("Good Morning, Alice")
print("Good Morning, Bob")
print("Good Morning, Charlie")
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
def hello(name):
    # Only have to change the message in one location
    print("Good Morning, " + name)

hello("Alice")
hello("Bob")
hello("Charlie")
```

---

# Keeping it DRY

```python
def hello(name):
    print("Good Morning, " + name)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    # If we ever want to call a different function we only have to change one line
    hello(name)
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
def volume(x, y, z):
    print("The volume is " + str(x * y * z))

volume(12, 3, 4)
volume(6, 14, 10)
```

---

# Functions — Parameters

```python
def <function_name>(<param_1>, <param_2>, ...):
    <your code here>
```

---

# [fit] Coding Time
## Section A

---

# Functions — Print vs Return

- print is a function you call. Use print when you want to show a value to a human.

- return is a keyword. When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called. Use return when you want to send a value from one point in your code to another.

- Using return changes the flow of the program. Using print does not.

---

# Functions — Returning

```python
def volume(x, y, z):
    return x * y * z

cube1 = volume(12, 3, 4)
cube2 = volume(6, 14, 10)
```

---

# Functions — Returning

```python
def <function_name>(<param_1>, <param_2>, ...):
    <your code here>

    return <value>
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

# Functions — Single Job

```python
def is_odd(number):
    if number % 2:
        return True

    return False
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
print("The factorial of " + str(num) + " is " + str(calc_factorial(num)))
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

# [fit] Coding Time
## Section B
