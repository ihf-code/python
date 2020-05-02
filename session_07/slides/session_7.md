# [fit] IHF: Code
## Python — Session 4

---

# Review

---

# Collections

- List
- Tuple
- Set
- Dictionary

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

# [fit]Questions?

---

# Functions

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

[.code-highlight: 4]
```python
def hello_world():
    print("Hello World!")

hello_world()
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
def area(x, y, z):
    print("The area is " + str(x * y * z))

area(12, 3, 4)
area(6, 14, 10)
```

---

# Functions — Parameters

```python
def <function_name>(<param_1>, <param_2>, ...):
    <your code here>
```

---

# [fit]Coding Time
## Section A

---

# Functions — Returning

```python
def area(x, y, z):
    return x * y * z

cube1 = area(12, 3, 4)
cube2 = area(6, 14, 10)
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

# [fit]Coding Time
## Section B

---

# Exercises

Finish off any exercises you did not complete in the session

---
## Any Questions

### go to sli.do #ihfcode