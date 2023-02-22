# KPMG:Code - Session 6 - Multiple Choice Questions

1. What is a dictionary in Python?
- a way to allow user input
- a statement that allows a computer to make a decision
- a way to print an output
- a collection of data - A

2. What brackets does a dictionary use?
- {} - A
- ()
- []
- <>

3. A dictionary is an unordered collection of data.
- True - A
- False

4. A tuple can be modified
- True
- False - A

5. What will be the output of the below:
shirt = {
    "size": "Large",
    "colour": "Red"
}

print(shirt["size"])

- size
- colour
- Large - A
- Red

6. What would be the output of the below:
contacts = [
    {"fname": "Ada", "lname": "Lovelace"},
    {"fname": "Alan", "lname": "Turing", "phone": "555-1234"},
    {"fname": "Steve", "lname": "Shirley"}
]

for person in contacts:
    if "phone" in person:
        print(person["fname"])

- Ada
- Alan - A
- Steve
- 555-1234

7. What will stop this while loop:
contacts = []
fname = None

while fname != "":
    fname = input("What is your first name? ")
    lname = input("What is your last name? ")

    if fname and lname:
        contacts.append({
            "fname": fname,
            "lname": lname
        })

- nothing, it will run forever
- entering a first name  
- not entering a first name - A
- not entering a first name and last name

8. Items in a dictionary are called _____ pairs.

- key, value - A
- value, key
- key, arguments
- value, arguments   

9. What will be the result of the below:

shirt = {
    "size": "Large",
    "colour": "Red"
}

shirt["colour"] = "Green"

- adds a new key/value
- changes an existing value - A
- deletes the key/value pair
- prints out the dictionary

10. What will be the result of the below:

shirt = {
    "size": "Large",
    "colour": "Red"
}

del(shirt["size"])

- adds a new key/value
- changes an existing value
- deletes the key/value pair - A
- prints out the dictionary
