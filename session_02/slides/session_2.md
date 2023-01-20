# [fit] KPMG: Code
## [fit] Python — Session 2 — Lesson

---

# Review

---

# Text Editor

### https://replit.com

---

# Hello World

```python
print("Hello, World!")
print("Hello, Saf!")
print("Hello, Jake!")
```

---

# Variables

```python
name = "Charlie"
age = 27
left_to_pay = 29.99
has_paid = False
```

---

# Variables

- Any mix of letters, numbers and some special characters
- Must start with a letter
- Keep lowercase
- Use underscore where there are spaces

---

# Data Types

Strings - Characters surrounded by quotes - "animal"
Integer - A whole number - 6
Float - A decimal number - 7.8
Boolean - True or False
None - Absence of a value

---

# Escaping

```
\n = New line
\t = Tab
\" = Double Quote
```

```python
favourite_food = "Pizza from \"Dough N' Sauce\""
shopping_list = "Apples\nBread\nMilk\nEggs"
```

---

# Numerical Operators

| Operator | Action | Example |
| --- | --- | --- |
| + | Addition | `1 + 2` |
| - | Subtraction | `3 - 1` |
| * | Multiplication | `3 * 7` |
| / | Division | `9 / 3` |
| ** | Exponent | `4 ** 2` |
| % | Modulus (remainder) | `10 % 3` |

---

# Concatenation

[.code-highlight: 1-2]
[.code-highlight: 3]
[.code-highlight: 1,5]
[.code-highlight: 1-3,6]
```python
first_name = "Bob"
last_name = "Jones"
full_name = first_name + " " + last_name

print("Hello " + first_name)
print("Good morning, " + full_name)
```

---

# Order of Operations

| | | |
| --- |--- | --- |
| Highest | () | Brackets |
| | ** | Exponent |
| | * | Multiplication |
| | / | Division |
| | + | Addition |
| Lowest | - | Subtraction |

---

## Any Questions?

---

# Comments

---

# Comments

[.code-highlight: 1-2]
[.code-highlight: 4]
```python
# The total including VAT
total = sub_total + vat

has_paid = False # If the user has paid or not
```

---

# Casting

---

# Casting — Integers

```python
x = int(1)   # x will be 1
y = int(2.6) # y will be 2
z = int("3") # z will be 3
```

---

# Casting — Floats

```python
w = float(4)     # w will be 4.0
x = float(5.6)   # x will be 5.6
y = float("6")   # y will be 6.0
z = float("7.3") # z will be 7.3
```

---

# Casting — Strings

```python
x = str("abc8") # x will be 'abc8'
y = str(9)      # y will be '9'
z = str(10.0)   # z will be '10.0'
```

---

# Casting

```python
age = 21

# ERROR: TypeError: can only concatenate str (not "int") to str
print("You are: " + age + " years old")
```

---

# Casting

```python
age = 21

# Cast the age integer to a string
print("You are: " + str(age) + " years old")
```

---

# Casting

```python
total = 79.99

# Cast the total float to string
print("Your order total is:" + str(total))
```

---

# Casting

```python
number_of_students = 32
number_of_girls = 19
percent_girls = int(number_of_girls / number_of_students * 100)
percent_boys = float(100 - percent_girls)

# Cast the different int/float values to string
print(str(percent_girls) + "% of the class are girls") # 59%
print(str(percent_boys) + "% of the class are boys") # 41.0%
```

---

# Length

---

# Length

[.code-highlight: 1-2]
[.code-highlight: 4]
```python
name = "Alice"
name_length = len(name) # 5

sentence_length = len("Hello, World!") #13
```

---

# Index

---

# Index

| H | e | l | l | o |
| --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 |

---

# Index

| C | H | A | R | L | I | E |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |

```python
name = "CHARLIE"
print(name[0]) # Prints 'C'
print(name[1]) # Prints 'H'
```

---

# Index

| H | e | l | l | o |
| --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 |
| -5 | -4 | -3 | -2 | -1 |

---

# Index

| A | L | I | C | E |
| --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 |
| -5 | -4 | -3 | -2 | -1 |

```python
print("ALICE"[4]) # Prints 'E'
print("ALICE"[-1]) # Prints 'E'
print("ALICE"[-3]) # Prints 'I'
```

---

# Index

| D | A | V | E |
| --- | --- | --- | --- |
| 0 | 1 | 2 | 3 |
| -4 | -3 | -2 | -1 |

```python
name = "Dave"
print(name[0]) # Always the first element
print(name[-1]) # Always the last element
```

---

# Input

---

# Input

```python
name = input("What's your name? ")

print("Hello " + name)
```

---

# Input

```python
age = int(input("How old are you? "))
age_in_10_years = age + 10

print("In 10 years you will be " + str(age_in_10_years))
```

---

# Input

```python
radius = float(input("What is the radius? "))
pi = float(input("What is the value of pi? "))
area = pi * (radius ** 2)

print("The area of the circle is: " + str(area))
```

---

# Upper/Lower

---

# Upper/Lower

[.code-highlight: 1-2]
[.code-highlight: 4]
```python
name = "Alice"
print(name.upper()) # ALICE

print("HeLlO".lower()) # hello
```

---

# Slicing

---

# Slicing

```
# slicing from one point to another
"string"[0:6] #string
"string"[1:4] #tri

# slicing from one point to the end
"string"[0:] #string
"string"[3:] #ing

# slicing from the start to another point
"string"[:0] #
"string"[:2] #st

# slicing from the start to end, by skipping step
"string"[0:6:2] #srn
```
---

# Putting it together

```python
fname = input("What's your first name? ")
lname = input("What's your last name? ")
# Calculate the total length of the users name
length = len(fname) + len(lname)

# Get the first letters of each part of the name and make uppercase
print("Your initials are " + fname[0].upper() + lname[0].upper())
print("Your full name is " + str(length) + " letters long")

# Get the middle letter in the full name as a lowercase string
# Index requires an integer, so we cast to prevent 5 / 2 = 2.5 — it will equal 2 instead
fullname = fname + lname
middle_letter = fullname[int(length / 2)].lower()

print("The middle letter of your name is " + middle_letter)
```

---

# [fit] Coding Time
## Section A
