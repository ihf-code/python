# [fit] IHF: Code
## Python — Session 5

---

# Review

---

# Functions

---

# Functions — Create

```python
def hello_world():
    print("Hello World!")
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

# Functions — Returning

```python
def area(x, y, z):
    return x * y * z

cube1 = area(12, 3, 4)
cube2 = area(6, 14, 10)
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
print("The factorial of " + num + " is " + str(calc_factorial(num)))
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

___

# [fit]Questions?

---

# Files

---

# Files — Open
```python
f = open("my_file.txt", "r")
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

# [fit]Coding Time
## Section A
```
cd kpmg-python-course/session_5/examples/
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
```

---

# Files — Write

[.code-highlight: 5-7]
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

# [fit]Coding Time
## Section B

---

# Exercises

Finish off any exercises you did not complete in the session

---

### Further Help

## [fit]DL-UKIHFCode@kpmg.co.uk
