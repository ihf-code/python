# A6 - The offer has now expired, remove the key/value for offer from the dictionary.
apple = {
    "Type": "Bramley",
    "Price": 0.39,
    "Colour": "Green",
    "Offer": True
}

del(apple["Offer"])
print(apple)
