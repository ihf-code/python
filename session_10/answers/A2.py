# 2. Create a Circle class, initialise it with a radius. Create two methods for the Circle class: get_area() and get_circumference() which give both respective areas and circumference.
#  - Note: Area of a circle = πr ** 2 
#  - Circumference = 2πr

class Circle:
    pi = 3.14159265
    
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print(self.pi * (self.radius ** 2))

    def get_circumference(self):
        print(self.pi * (self.radius * 2))

circy = Circle(11)
circy.get_area()

circy = Circle(4.44)
circy.get_circumference()