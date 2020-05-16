# [fit] IHF: Code
## Python — Session 10

---

# Review

---

# Object Oriented Programming 

---
# Object Oriented Programming 
Before OOP, most programs were a list of instructions that acted on memory in the computer. 
OOP, however, is modeled around objects that interact with each other. 
Python is an OOP language. 

---

# Class 

---
# Class 
A class is the blueprint for an object. 

---

# Class 

```python
class Name_of_your_class:
    <your code here>
```

---

# Class

```python
class Car:
	wheels = 4 
```

---

# Object 

---
# Object 
An object, is an instance of that class.
It uses the blueprint of class to create its own object. 

---

# To instantiate an object
Instantiating an object is creating an object from the class. 

```python
class Car:
	wheels = 4

volvo = Car()
```
---

# Object 

```python
class Car:
	wheels = 4

volvo = Car()
print(volvo.wheels)

```
---

# The self parameter  

---
# The self parameter 
The self parameter allows you to pass variables from the class when instantiating the object 

---
# The self parameter 

```python
class Car:
	wheels = 4
    
    def get_wheels(self):
		# This wouldn't work as you require 'self.' 
        # if you are pulling the variable from the class
        print(wheels) 

```
---
# The self parameter 

```python
class Car:
	wheels = 4
    
    def get_wheels(self):
        print(self.wheels) 

```
---
# The self parameter 

```python
class Car:
	wheels = 4
    
    def get_wheels(self):
        print(self.wheels) 

mercedes = Car()
mercedes.get_wheels()

```
---

# [fit]The __ init __ function

---
# The __ init __ function

All classes have a built-in function called __init__()
This is always the first function executed when the class is being initiated.

---
# The __init __ function

```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour 
    self.miles = miles

volvo = Car("red", 30000)

print(volvo.colour)
print(volvo.miles)

```
---

# Class variables vs instance variables

---

# Object Methods

---
# Object Methods
Methods in objects are functions that belong to the object.

---
# Object Methods
```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour 
    self.miles = miles
  
  #This is the object method 
  def car_information(self):
    print("This car is " + self.colour + " and has " + str(self.miles) + " miles.")

volvo = Car("red", 30000)

print(volvo.colour)
print(volvo.miles)
volvo.car_information()

```
---

# Modify Object Properties

```python
volvo = Car("red", 30000)

print(volvo.colour) #red 

volvo.colour = “blue” 

print(volvo.colour) #blue

```

---

# Delete Object Properties

```python
volvo = Car("red", 30000)

print(volvo.miles) #30000 

del volvo.miles 

print(volvo.miles) #AttributeError: 'Car' object has no attribute 'miles'

```

---

# The pass statement

---

# The pass statement
If have a class definition with no content, put in the pass statement to avoid getting an error.

---

# The pass statement
```python
class Car:
    pass

```

---

# [fit]Questions?

---

# Inheritance

---

# Parent Class

---

# Parent Class

The parent class is the class being inherited from.
Any class can be a parent class, so the syntax is the same as creating any other class.

---

# Parent Class 

```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour 
    self.miles = miles
  
  def car_information(self):
    print("This car is " + self.colour + " and has " + str(self.miles) + " miles.")

volvo.car_information() # This car is red and has 30000 miles.

```
---

# Child Class

---

# Child Class

Child class is the class that inherits from another class
To create a child class, you pass the parent class as a parameter. 

---

# Child Class
```python
class Volvo(Car): 
    pass      
```

---

# Child Class

The child class (Volvo) has the same methods and properties as the parent class (Car).

---

# Child Class

```python
class Car:
  wheels = 4

  def __init__(self, colour, miles):
    self.colour = colour 
    self.miles = miles
  
  def car_information(self):
    print("This car is " + self.colour + " and has " + str(self.miles) + " miles.")

class Volvo(Car):
  pass

volvo_s90 = Volvo("black", 20000)
volvo_s90.car_information() # This car is black and has 20000 miles.

```
---

# The __ init __ function

When you add the __ init __ function to the child class, it no longer inherits the parents. 

---

# The __ init __ function

```python
class Volvo(Car):
  def __init__(self, colour, miles):

```
---
# The __ init __ function

To keep the parent's __ init __ function, add a call to the parent's  __ init __ function. 

---
# The __ init __ function

```python
class Volvo(Car):
  def __init__(self, colour, miles):
    Car.__init__(self, colour, miles):
```

---

# The super() function

The super function will make the child class inherit all the methods and properties from its parent.

--- 

# The super() function

```python
class Volvo(Car):
  def __init__(self, colour, miles, seats):
    super().__init__(colour, miles)

```
---

# Adding properties to the child class

```python
class Volvo(Car):
  def __init__(self, colour, miles, seats):
    super().__init__(colour, miles)
    #Adding another property to the child class
    self.seats = seats 

volvo_s90 = Volvo("black", 20000, 5)
print(volvo_s90.seats)


```
---

# Adding methods to the child class

```python
class Volvo(Car):
  def __init__(self, colour, miles, seats):
    super().__init__(colour, miles)
    self.seats = seats 
  
  #Adding another method to the child class
  def more_car_info(self):
    print("This car is " + self.colour + ", has " + str(self.miles) +
    " miles and " + str(self.seats) + " seats.")

volvo_s90 = Volvo("black", 20000, 5)
volvo_s90.more_car_info()


```

---

# Questions

# sli.do #ihfcode

---