# [fit] IHF: Code
## Python — Session 2

---

# Review

---

# Text Editor

### http://repl.it

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

# Input

---

# Input

[.code-highlight: 1-2]
[.code-highlight: 4-6]
```python
name = input("What's your name? ")
print("Hello " + name)

age = int(input("How old are you? "))
age_in_10_years = age + 10
print("In 10 years you will be " + str(age_in_10_years))
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

# [fit]Coding Time
## Section A

---

- 1. Create two variables, a variable that hold the width of a rectangle and a variable that holds height of a rectangle, work out and store the area in a third variable. Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`
- 2. Write code that prints the length of the string, 'python'
- 3. Print out the first and third letter of the word 'python'

---

- 4. Ask the user to enter their name, and print out `Hello, <name>`
- 5. Ask the user to enter their age, tell them how old they will be in 15 years time
- 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. In 15 years time you will be <age_in_15_years_time>`
- 7. Ask the user to enter their hometown, print it out in uppercase letters

---

- 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
- 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

---

- 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string, `It is <month> and the average temperature is <average temperature> degrees celsius`
- 11. Print out the above sentence but make the month upper case
- 12. Create a variable that holds your favourite animals and print it out. Make sure the animals are all on different lines and tabbed
- 13. Ask the user to enter their name as well as a number. Print out the uppercase character at that position in the string

---
## Any Questions

### go to sli.do #ihfcode
