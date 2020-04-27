# Integer examples
x = int(1)   # x will be 1
y = int(2.6) # y will be 2
z = int("3") # z will be 3

# Float examples
w = float(4)     # w will be 4.0
x = float(5.6)   # x will be 5.6
y = float("6")   # y will be 6.0
z = float("7.3") # z will be 7.3

# String examples
x = str("abc8") # x will be 'abc8'
y = str(9)      # y will be '9'
z = str(10.0)   # z will be '10.0'

# Cast an integer to a string
age = 49
age_as_string = str(age)
print("They are " + age_as_string)

# Cast integer to string all in one line
print("They are " + str(age))

# Cast float to int
pi = 3.14159
print(pi)
print(int(pi))

# Accept user input as a string and convert to integer
age = int(input("How old are you? "))
age_10_years_ago = age - 10
print(age_10_years_ago)

# Get user input as a float
amount = float(input("What is the total amount in £? "))
vat = 20
vat_amount = (amount / 100) * vat
print(vat_amount)
