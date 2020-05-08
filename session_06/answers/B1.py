# B1 - Ask the user to enter a persons name, if they enter a name, ask for the persons age.
# Store this information in a dictionary inside a list.
# Continue to ask for names until no name is given.
# Then print out all of the names and ages collected

contacts = []
fname = None
 
while fname != "":
    fname = input("What is your first name? ")
    if fname:
        age = int(input("What is your age? "))
        contacts.append(
            {
                "fname": fname,
                "age": age
            }
        )
print(contacts)