
# 4. Create a Vehicle parent class, initialise it with, wheels, colour and a method to display all this information.
#     - i. Create a Tesla (or any car brand) child classs and add a method to get the miles and a method to display all this information.
#     - ii. Change the colour of the vehicle.
#     - iii. Delete the wheels.

class Vehicle:
    def __init__(self, wheels, colour):
        self.wheels = wheels
        self.colour = colour

    def display_info(self):
        print("This car is " + self.colour + " and has " + str(self.wheels) + " wheels.")


class Tesla(Vehicle):
    def __init__(self, wheels, colour, miles):
        super().__init__(wheels, colour)
        self.miles = miles

    def display_more_info(self):
        print("This car is " + self.colour + " and has " + str(self.wheels) + " wheels and " + str(self.miles) + " miles.")


tesla = Tesla(4, "black", 20000)
tesla.display_more_info()

tesla.colour = "red"
tesla.display_more_info()

del tesla.wheels
tesla.display_more_info()
