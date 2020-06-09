# 2. Create a Circle class, initialise it with a radius. Create two methods for the Circle class: get_area() and get_circumference() which give both respective areas and circumference, to 2 decimal placese.
# - Note: Area of a circle = πr ** 2
# - Circumference = 2πr
# - Use the round() function to get the answer to 2 decimal places


class Circle:
    pi = 3.14159265

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print("Area: " + str(round(self.pi * (self.radius ** 2), 2)))

    def get_circumference(self):
        print("Circumference: " + str(round(self.pi * (self.radius * 2), 2)))


circle1 = Circle(9)
circle1.get_area()
circle1.get_circumference()

circle2 = Circle(6.87)
circle2.get_area()
circle2.get_circumference()
