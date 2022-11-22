# [fit] KPMG: Code
## [fit] Python — Session 8 — Lesson

---

# Review

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
def hello(name):
    print("Hello, " + name + "!")

hello("Alice")
hello("Bob")
hello("Charlie")
```

---

# Keeping it DRY

```python
def hello(name):
    print("Good Morning, " + name)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    # If we ever want to call a different function we only have to change one line
    hello(name)
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
def volume(x, y, z):
    print("The volume is " + str(x * y * z))

volume(12, 3, 4)
volume(6, 14, 10)
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

## Any Questions?

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

# [fit] Coding Time
## Section A

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

# [fit] Coding Time
## Section B

