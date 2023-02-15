# [fit] KPMG: Code
## [fit] Python — Session 3 — Lesson

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

```python
first_name = "Bob"
last_name = "Jones"
full_name = first_name + " " + last_name

print("Hello " + first_name)
print("Good morning, " + full_name)
```

---

# Comments
```python
# The total including VAT
total = sub_total + vat

has_paid = False # If the user has paid or not
```

---

# Casting

```python
x = int(8.3)  # x will be 8
y = float(9)  # y will be 9.0
z = str(10.0) # z will be '10.0'
```

---

# Index


| A | L | A | N | T | U | R | I | N | G |
| --- | --- | --- | --- | --- | --- | --- | -- | -- | -- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |



```python
fullname = "Alan" + "Turing"
length = len(fullname) # 10
# int(length / 2) = 5
middle_letter = fullname[5].lower()
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

## Any Questions?

---

# Conditionals

---

# If

---

# If

```python
if True:
    print("This is always shown")

if False:
    print("This is never shown")    
```

---

# If

```python
if <expression>:
    # Will only be run if the expression is True
    <code>
```

---

# Indenting

---

# Indenting

```python
name = "Alice"

if name == "Alice":
    print("Hello Alice")
```

---

# Indenting

```python
name = "Alice"

if name == "Alice":
    print("Hello Alice")
    print("How are you?")

print("Thanks")
```

---

# Comparators

| Comparator |  Description | Example |
|--- | --- | --- |
| == | Equals | "Alice" == "Alice"
| != | Does not equal | "Bob" != "Charlie"
| < | Less than | 4 < 10
| > | Greater than | 12 > 8
| <= | Less than or equal to | 7 <= 7
| >= | Greater than or equal to | 8 >= 5

---

# Comparators

```python
name = "Alice"

if name == "Alice":
    print("Hello Alice")

if name != "Charlie":
    print("You are not Charlie")
```

---

# Comparators

```python
age = 20

if age > 17:
    print("You can vote")

if age >= 21:
    print("You are 21 or over")
```

---

# Else

---

# Else

```python
if 1 == 1:
    print("Yes")
else:
    print("No")    
```

---

# Else

```python
if <expression>:
    # Will only be run if the expression is True
    <code>
else:
    # Catchall block that will be run if the expression is False
    <code>
```

---

# Else

```python
name = "Alice"

if name == "Alice":
    print("Hello Alice")
else:
    print("You're not Alice")
```

---

# Else

```python
age = 15

if age >= 21:
    print("You are 21 or over")
else:
    print("You are 20 or younger")
```

---

# [fit] Coding Time
## Section A

---

# Elif

---

# Elif

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

# Elif

```python
age = int(input("How old are you? "))

if age <= 13:
    print("You are 13 or younger")
elif age < 18:
    print("You are between 14 and 17")
elif age == 18:
    print("You are 18")
else:
    print("You are 19 or over")
```

---

# Elif

```python
age = int(input("How old are you? "))

if age <= 13:
    print("You are 13 or younger")
elif age < 18:
    print("You are between 14 and 17")
elif age == 0:
    # This will never get run
    print("You aren't born yet")
else:
    print("You are 19 or over")
```

---

# Elif

```python
age = int(input("How old are you? "))

if age == 0:
    # This will now run as expected
    print("You aren't born yet")
elif age <= 13:
    print("You are 13 or younger")
elif age < 18:
    print("You are between 14 and 17")
else:
    print("You are 19 or over")
```

---

# And, Or, Not

---

# And, Or, Not

```python
if age > 12 and age < 20:
    print("You are a teenager")

if age < 13 or age > 19:
    print("You are not a teenager")

if not (age > 12 and age < 20):
    print("You are not a teenager")
```

---

# [fit] Coding Time
## Section B
