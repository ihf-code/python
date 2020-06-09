# 1. Create a Person class, initialise it with a name. Create a method for the Person class that will say hello to the name.

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name)


saf = Person("Saf")
jake = Person("Jake")

saf.hello()
jake.hello()
