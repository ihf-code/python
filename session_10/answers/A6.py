# 6. Create a Sandwich class with the attributes order_number and ingredients.
# - i. The ingredients attributes is given as a list - (Note: use list(<atrribute>) to enable this).
# - Only the ingredients attributes will be given as input.
# - ii. The order attriubte will be a method that counts the order number.
# - iii. Make three methods for the following favourite sandwiches, for customers who don't want to create a sandwich:
# - vegan_hot - vegan cheese, meatless meatballs, jalapenos
# - meat_feast - steak, peppers, cheese
# - veggie - tomamto, spinach, mushroom, eggs

class Sandwich:
    orders = 0

    def __init__(self, ingredients):
        self.ingredients = list(ingredients)
        self.order_number = self.get_order_number()

    def get_order_number(self):
        Sandwich.orders += 1
        return Sandwich.orders

    def vegan_hot():
        return Sandwich(["vegan cheese", "meatless meatballs", "jalapenos"])

    def meat_feast():
        return Sandwich(["steak", "peppers", "cheese"])

    def veggie():
        return Sandwich(["tomato", "spinach", "mushroom", "eggs"])


sandwich1 = Sandwich.vegan_hot()
print(sandwich1.ingredients)
print(sandwich1.order_number)

sandwich2 = Sandwich(["tuna", "mayo", "lettuce"])
print(sandwich2.ingredients)
print(sandwich2.order_number)
