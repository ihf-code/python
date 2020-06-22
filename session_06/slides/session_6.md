# [fit] IHF: Code
## [fit] Python — Session 6 — Lesson
### Live at 10am

---

# Review

---

# List
```python
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]

print(days)
# ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]

print(days[1]) # Tue
```
---

# List

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
# Create variables to store our numbers and counts
numbers = [1, 10, 13 , 15, 765, 32, 65, 23, 56, 101]
even_count = 0
odd_count = 0

# Loop through all our numbers
for i in numbers:
    # Check to see if the number is odd/even
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        # This is short hand for the line above
        odd_count += 1

print("Even: " + str(even_count))
print("Odd: " + str(odd_count))
```

---

# For Loops

```python
for letter in "supercalifragilisticexpialidocious":
    print(letter.upper())
```

---

# Ranges

[.code-highlight: 1-2]
[.code-highlight: 4-5]
[.code-highlight: 7-8]
```python
range(10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range(1, 5)
#[1, 2, 3, 4]

range(2000, 2020, 4)
#[2000, 2004, 2008, 2012, 2016]
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

# Modules

```python
import random
from math import floor
```

---

# Random Module

```python
import random

# Random float from 0.0 to 1.0
print random.random()

# Gets a random number between 1 and 10
number = random.randint(1, 10)

# Gets a random choice from a list
number = random.choice(["Rock", "Paper", "Scissors"])
```

---

# Math Module

```python
from math import floor, ceil

number = floor(3.2) # 3
print(floor(9.99)) # 9

number = ceil(3.2) # 4
print(ceil(9.99)) # 10
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
    x = x + 1

for y in range(1, 101):
    print(y)
```

---

# While Loops

```python
age = -1

# Keep asking for their age until they enter a sensible value
while age < 0 or age > 130:
    age = int(input("How old are you? "))

print("You are: " + str(age))
```

---

# Shorthand Arithmetic

```python
number = 3
number += 5 # 8
number -= 2 # 6
number *= 4 # 24
number /= 2 # 12
number **= 2 # 144
```

---

# Infinite Loops

```python
while True:
    # This loops forever
    print("Hello")
```

---

# Break Statements

```python
while True:
    print("Hello")
    break
```

---

# Break Statements

```python
times_to_loop = int(input("How many times should I loop? "))

for x in range(times_to_loop):
    print("Hello")
    # x starts at 0, so to break after 5 loops we do this
    if x >= 4:
        break
```

---

## Any Questions?
### sli.do #ihfcode

---

# Collections

---

# Collections

List

Tuple

Set

Dictionary

---

# Collections — Tuple

```python
colours = ("Red", "Blue", "Green")
print(colours[0]) # Red
print(colours[1]) # Blue
print(colours[2]) # Green
```

---

# Collections — List Vs Tuple

A tuple is the same as list except you can't change it after creation.

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

student = {
    "name": "Alice Smith",
    "year": "9",
    "form_tutor": "Miss Mirza"
}
```


---

# Collections — Dictionary

```python
my_dict = {
    "<key>": "<value>",
    "<key2>": "<value>",
    ...
}
```

---

# Dictionary

```python
shirt = {
    "size": "Large",
    "colour": "Red"
}
print(shirt["size"]) # Large
print(shirt["colour"]) # Red
```

---

# Dictionary — Append

```python
shirt = {
    "size": "Large",
    "colour": "Red"
}

# Add a new key/value
shirt["material"] = "Cotton"
```

---

# Dictionary — Change

```python
shirt = {
    "size": "Large",
    "colour": "Red",
    "material": "Cotton"
}

# Change the colour of the shirt
shirt["colour"] = "Green"
```

---

# Dictionary — Delete

```python
shirt = {
    "size": "Large",
    "colour": "Green",
    "material": "Cotton"
}

# Delete the key/value
del(shirt["size"])
```

---

# Dictionary — In

```python
shirt = {
    "colour": "Green",
    "material": "Cotton"
}

# Check to see if the key "material" exists in the dictionary
if "material" in shirt:
    print("The material is: " + shirt["material"])
```

---

# Dictionary — For

```python
shirt = {
    "colour": "Green",
    "material": "Cotton"
}

for key in shirt:
    print(str(key) + " = " + str(shirt[key]))
```

---

# Collections

| Collection |  Ordered | Changeable | Duplicates | Key |
|--- | --- | --- | --- | --- |
| List | Yes | Yes | Yes | No
| Tuple | Yes | No | Yes | No
| Set | No | Yes | No | No
| Dictionary | No | Yes | No | Yes

---

# [fit] Coding Time
## Section A

---

# Nested Collections

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

# Adding names

```python
contacts = []
fname = None

while fname != "":
    fname = input("What is your first name? ")
    lname = input("What is your last name? ")

    if fname and lname:
        contacts.append({
            "fname": fname,
            "lname": lname
        })
```

---

# [fit] Coding Time
## Section B

---

### Questions?
### go to sli.do #ihfcode

---

# [fit] Next Session
### Thursday 14th May 2pm
### Answers
