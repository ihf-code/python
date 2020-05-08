#Create a menu with 5 items.  
# Store this information in a dictionary inside a list. 
# Each item in the menu should have the name of the item, the price and if its vegetarian friendly (make at least one vege friendly dish). 
# Print out the entire menu. 
# Print out the name of the vegetarian option(s). 

menu = [
      {
        "name": "tofu fritters",
        "price": 5.99,
        "vegetarian_friendly": True
      },
      {
        "name": "black bean curry",
        "price": 6.25,
        "vegetarian_friendly": True
      },
      {
        "name": "shepherds pie",
        "price": 9.99,
        "vegetarian_friendly": False
      },
      {
        "name": "cheese and potato pie",
        "price": 5.00,
        "vegetarian_friendly": True
      },
      {
        "name": "fries",
        "price": 0.99,
        "vegetarian_friendly": True
      }
    ]

# print(menu)
for dish in menu:
  if dish["vegetarian_friendly"]:
    print(dish["name"])

