# [fit] IHF: Code
## Python — Session 3

---

# Review

---

# List

```python
names = ["Alice", "Bob", "Charlie"]

print(names[1]) # Bob

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

# [fit]Questions?

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
print random.random()

# Gets a random number between 1 and 10
number = random.randint(1, 10)
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

# Infinite Loops

---

# Infinite Loops

```python
while True:
    # This loops forever
    print("Hello")
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

# [fit]Coding Time
## Section A

---

## Any Questions

### go to sli.do #ihfcode
