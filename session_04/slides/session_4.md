# [fit] KPMG: Code
## [fit] Python — Session 4 — Lesson

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

# Order matters

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

# Order matters

```python
age = int(input("How old are you? "))
if age == 0:
    # This expression gets evaluated and runs
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

```python
if age > 12 and age < 20:
    print("You are a teenager")

if age < 13 or age > 19:
    print("You are not a teenager")

if not (age > 12 and age < 20):
    print("You are not a teenager")
```

---

## Any Questions?

---

# List

---

# List

```python
names = ["Alice", "Bob", "Charlie"]
print(names[0]) # Alice
print(names[1]) # Bob
print(names[2]) # Charlie
```

---

# List — Append

```python
names = ["Alice", "Bob", "Charlie"]

# Append a new value to the end of the list
names.append("Dave")

print(names) # ["Alice", "Bob", "Charlie", "Dave"]

```

---

# List — Change

```python
names = ["Alice", "Bob", "Charlie"]

# Change the value stored in index 2
names[2] = "Chris"

print(names) # ["Alice", "Bob", "Chris"]

```

---

# List — Delete

```python
names = ["Alice", "Bob", "Charlie"]

# Delete the item at index 1
del(names[1])

print(names) # ["Alice", "Charlie"]

```

---

# List — In

```python
names = ["Alice", "Bob", "Charlie"]

# Check to see if "Eve" is in the list
if "Eve" in names:
    print("Eve is here")
else:
    print("Eve isn't here")
```

---

# List — Length

```python
names = ["Alice", "Bob", "Charlie"]

# Get the number of items in the list
print(len(names)) # 3
```

---

# List — Sort

```python
names = ["Charlie", "Alice", "Bob"]

# Sort the items in the list alphabetically
names.sort()

print(names) # ["Alice", "Bob", "Charlie"]
```

---

# [fit] Coding Time
## Section A

---

# For Loops

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
for <item> in <items>:
    # Runs once for each item in items
    <code>
```

---

# For Loops

```python
for my_number in range(5):
    print(my_number)

# 0
# 1
# 2
# 3
# 4
```

---

# Ranges

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

# [fit] Coding Time
## Section B
