# [fit] KPMG: Code
## [fit] Python — Session 5 — Lesson
---

# Review

---

# List
```python
names = ["Alice", "Bob", "Charlie"]

days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]

# Can be spread out over multiple lines
colours_of_rainbow = [
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Indigo",
    "Violet"
]
```
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
numbers = [1, 10, 13, 15, 765, 32, 65, 23, 56, 101]
even_count = 0
odd_count = 0

# Loop through all our numbers
for i in numbers:
    # Check to see if the number is odd/even
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

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

# For Loops

```python
# All vowels in lowercase
vowels = ["a", "e", "i", "o", "u"]

# Make the word lowercase and then loop through each letter
for letter in "supeRcaliFragiListiCexPiaLidOcIous".lower():
    # Check to see if the lowercase letter matches a vowel
    if letter in vowels:
        print(letter.upper())
    else:
        print(letter.lower())
```

---

# Ranges

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
# Do something 3 times
for x in range(3):
    print(input("What is your name? "))
```

---

# For Loops

```python
times_to_ask = int(input("How many times should I ask? "))

for x in range(times_to_ask):
    print(input("What is your name? "))
```

---

## Any Questions?

---

# Modules

---

# Modules

```python
import random
from math import floor
```

---

# Modules

```python
import <module>
from <module> import <function>

<rest of code>
```

---

# Random Module

---

# Random Module

```python
import random

# Random float from 0.0 to 1.0
print(random.random()) # 0.38469447

# Gets a random number between 1 and 10
number = random.randint(1, 10)
print(number) # 7
```

---

# Random Module

```python
import random

students = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Remember that index start at 0 and end at one less than the number of items
index = random.randint(0, len(students) - 1)
print(students[index])
```

---

# Random Module

```python
import random

students = ["Alice", "Bob", "Charlie", "David", "Eve"]

print(random.choice(students))
```

---

# Math Module

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
while <condition>:
    # Runs over and over while condition is True
    <code>
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

# While Loops

```python
times_in_loop = 1
while times_in_loop <= 100:
    print(times_in_loop)
    times_in_loop = times_in_loop + 1

# ...
# 98
# 99
# 100
```

---

# While Vs For Loop

```python
x = 1
while x <= 100:
    print(x)
    times_in_loop = times_in_loop + 1

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

# While Loops

```python
times_in_loop = 0
while times_in_loop <= 10:
    print("Hello")
    # times_in_loop = times_in_loop + 1
    times_in_loop += 1
```

---

# Infinite Loops

---

# Infinite Loops

```python
while True:
    # This loops forever
    print("Hello")
```

---

# Infinite Loops

```python
times_in_loop = 0

# An error here causes this to run for ever
while times_in_loop >= 0:
    print("Hello")
    times_in_loop += 1
```

---

# Break Statements

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
times_in_loop = 0

while times_in_loop >= 0:
    print("Hello")
    times_in_loop += 1
    if times_in_loop > 100:
        break
```

---

# Break Statements

```python
# Only loops once as we break out
for x in range(1, 101):
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

# [fit] Coding Time
## Section A

---

### Questions?
