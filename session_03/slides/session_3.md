# [fit] IHF: Code
## [fit] Python — Session 3 — Lesson
### Live at 10am

---

# Review

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

```python
name = input("What's your name? ")
print("Hello " + name)

age = int(input("How old are you? "))
age_in_10_years = age + 10
print("In 10 years you will be " + str(age_in_10_years))
```

---

## Any Questions?
### sli.do #python2020

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

[.code-highlight: 1-6]
[.code-highlight: 8-10]
```python
name = "Alice"
if name == "Alice":
    print("Hello Alice")

if name != "Charlie":
    print("You are not Charlie")

age = 24
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
    # Will only be run if the expression is False
    <code>
```

---

# Else

[.code-highlight: 1-5]
[.code-highlight: 7-11]
```python
name = "Alice"
if name == "Alice":
    print("Hello Alice")
else:
    print("You are not Alice")

age = 15
if age >= 21:
    print("You are 21 or over")
else:
    print("You are 20 or younger")
```

---

# [fit]Coding Time
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
    # This can never be run
    print("You aren't born yet")
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

# [fit]Coding Time
## Section B


---

### Questions?
### go to sli.do #python2020

---

# [fit]Next Session
### Thursday 21st May 10am
### Answers
