# A5 - Print out all the key/value pairs of the apple.
apple = {
    "Type": "Bramley",
    "Price": 0.39,
    "Colour": "Green",
    "Offer": True
}

for key in apple:
    print(str(key) + " = " + str(apple[key]))
