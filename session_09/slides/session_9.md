# [fit] IHF: Code
## [fit] Python — Session 9 — Lesson
### Live at 10am

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

# While Loops

```python
guess = None
while guess != 4:
    # Continues to ask for a number until you enter 4
    guess = int(input("What's your number? "))
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

# Functions — Returning

```python
def volume(x, y, z):
    return x * y * z


cube1 = volume(12, 3, 4)
cube2 = volume(6, 14, 10)
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
### sli.do #python2020

---

# Multiple Assignment

---

# Multiple Assignment

```python
x, y = 10, 30

print(x) # 10
print(y) # 30
```

---

# Unpacking

```python
# All of these are the same
x, y = 10, 30
x, y = (10, 30)
(x, y) = 10, 30
(x, y) = (10, 30)
```

---

# Unpacking

```python
x, y = "hi"

print(x) # h
print(y) # i
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

# Returning multiple variables

```python
def order_total(subtotal):
    vat = 0.20
    vat_amount = subtotal * vat
    total = subtotal + vat_amount

    return (total, vat_amount, vat)


total, tax, vat = order_total(10.00)

# total = 12.0
# tax = 2.0
# vat = 0.2
```

---

# Enumerate

```python
f = open("names.txt", "r")

for i, line in enumerate(f):
    print("Line " + str(i) + ": " + line)

# Line 0: ...
# Line 1: ...
# Line 2: ...
# ...
```

---

# Enumerate

```python
names = ["Alice", "Bob", "Charlie", "Dave"]

for counter, value in enumerate(names):
    print(counter, value)
```

---

# Default Arguments

---

# Default Arguments

```python
def hello(name):
    print("Hello " + name)


hello("Jake")
hello("Saf")
hello() # Causes an error
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

# Default Arguments

```python
def circle_area(r, PI = 3.14):
    return PI * (r ** 2)


print(circle_area(9.5)) # 283.385
print(circle_area(9.5, 3.141592)) #283.528678
```

---

# Keyword Arguments

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

# Keyword Arguments

```python
def add_result(player_1 = "Alice", player_2 = "Bob", player_1_score = 0, player_2_score = 0):
    # ...
    # Process the data passed in
    # ...


# Only set player 1 values
add_result(player_1 = "Jake", player_1_score = 8)
add_result(player_1 = "Saf", player_1_score = 42)

# Only set the scores
add_result(player_1_score = 3, player_2_score = 2)
```

---

# Keyword Arguments

```python
def send_message(to, from = "Alice", message = "Hi"):
    # ...
    # Send the message
    # ...


# Both the same as 'to' is first in the parameters
send_message("Saf")
send_message(to = "Saf")

# All the same
send_message("Jake", "Saf", "Where are you?")
send_message("Jake", message = "Where are you?", from = "Saf")
send_message(message = "Where are you?", to = "Jake", from = "Saf")
```

---

# \*args

---

# \*args — Arguments

```python
def count_numbers(a, b, c, d, e):
    return a + b + c + d + e

print(count_numbers(1, 3)) # Error
print(count_numbers(1, 3, 5)) # Error
print(count_numbers(1, 3, 5, 7)) # Error
print(count_numbers(1, 3, 5, 7, 9)) # 25
print(count_numbers(1, 3, 5, 7, 9, 11)) # Error
```

---

# \*args — Arguments

```python
def count_numbers(*args):
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
def count_numbers(*args):
    # args is just a list — so you can sum all the values
    return sum(args)

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

# \*\*kwargs

---

# \*\*kwargs — Keyword Arguments

```python
def my_func(**kwargs):
    print(kwargs)

my_func(name = "Jake", location = "Manchester")
# {'name': 'Jake', 'location': 'Manchester'}
```

---

# \*\*kwargs — Keyword Arguments

```python
def add_result(**kwargs):
    # ...
    # Process data
    # ...

    # Print the scores
    for key in kwargs:
        if key.endswith("_score"):
            print(kwargs[key])


add_result(
    player_1 = "Alice",
    player_1_score = 7,
    player_2 = "Bob",
    player_2_score = 42
)
```

---

# [fit] \*args & \*\*kwargs

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

# \*args & \*\*kwargs

```python
add_item(
    "13418",
    "IHF: Code — Intro to Python",
    "video",
    creator = "Jake & Saf",
    length = "1:12:00",
    year_created = "2020"
)
# ('13418', 'IHF: Code — Intro to Python', 'video')
# {'creator': 'Jake & Saf', 'length': '1:12:00', 'year_created': '2020'}
```

---

# \*args & \*\*kwargs

```python
def add_item(id, name, book, **kwargs):
    print(id, name, book)
    print(kwargs)


add_item(
    "18971", # internal ID
    "A guide to Python", # Item Name
    "book", # Item Type
    author = "Alice Smith",
    isbn = "1234567890123"
)

```

---

# Packing / Unpacking

---

# Packing / Unpacking

```python
numbers = [1, 3, 5, 7]
more_numbers = [*numbers, 9, 11, 13]

print(more_numbers)

# [1, 3, 5, 7, 9, 11, 13]
```

---

# Packing / Unpacking

```python
fruit_stock = {"apples": 15, "oranges": 30, "pineapples": 3}
latest_stock = {**fruit_stock, "apples": 21}

print(latest_stock)

# {'apples': 21, 'oranges': 30, 'pineapples': 3}
```

---

# Packing / Unpacking

```python
fruit_stock = {"apples": 15, "oranges": 30, "pineapples": 3}
delivery = {"mangos": 12, "bananas": 24}
latest_stock = {**fruit_stock, "apples": 21, **delivery}

print(latest_stock)

# {'apples': 21, 'oranges': 30, 'pineapples': 3, 'mangos': 12, 'bananas': 24}
```

---

# Packing / Unpacking

```python
def volume(x, y, z):
    return x * y * z

data = [
    {"x": 3, "y": 12, "z": 4}, # 144
    {"x": 6, "y": 9, "z": 8}, # 432
    {"x": 2, "y": 15, "z": 10}, # 300
]

for x in data:
    print(volume(**x))

# volume(x = 3, y = 12, z = 4)
# volume(x = 6, y = 9, z = 8)
# volume(x = 2, y = 15, z = 10)
```

---

# Packing / Unpacking

```python
def add_contact(**kwargs):
    for key, value in kwargs.items():
        print(key + " : " + value)


contact = {"fname": "Alice", "lname": "Smith"}
add_contact(**contact)

# add_contact(fname = "Alice", lname = "Smith")
```

---

# [fit] Coding Time
## Section A

---

### Questions?
### go to sli.do #python2020

---

# [fit] Next Session
### Thursday 9th July 10am
### Answers
