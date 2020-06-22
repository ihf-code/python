## Section 10 Exercises

# Section A
1. Create a class called Upper which has two methods called get_word and print_word.
    - the get_word method should accept a string from the user
    - the print_word method prints the string in upper case.
2. Create a Person class, initialise it with a name. Create a method for the Person class that will say hello to the name.
3. Create a Circle class, initialise it with a radius. Create two methods for the Circle class: get_area() and get_circumference() which give both respective areas and circumference, to 2 decimal placese.
- Note: Area of a circle = πr ** 2
- Circumference = 2πr
- Use the round() function to get the answer to 2 decimal places
4. Create a Employee class and initialise it with name and staff number.
    - i. Make methods to:
    - display_info - It should display all the information of the employee.
    - set_department - It should assign the department to employee.
    - set_bonus - It should assign a bonus amount to the employee.

    - ii. Create the instance attributes first name and last name instead of name.
    - Create two methods full_name and email_address in the Employee class.
    - Given a person's first and last names:
    - Form the full_name method by simply joining the first and last name together, separated by a space.
    - Form the email_address by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure everything is in lowercase.
    
5. Create a Vehicle parent class, initialise it with, wheels, colour and a method to display all this information.
     - i. Create a Tesla (or any car) child classs and add a method to get the miles and a method to display all this information.
     - ii. Change the colour of the vehicle.
     - iii. Delete the wheels.

6. Create a Sandwich class with the attributes order_number and ingredients.
- i. The ingredients attributes is given as a list - (Note: use list(<atrribute>) to enable this).
- Only the ingredients attributes will be given as input.
- ii. The order attriubte will be a method that counts the order number.
- iii. Make three methods for the following favourite sandwiches, for customers who don't want to create a sandwich:
- vegan_hot - vegan cheese, meatless meatballs, jalapenos
- meat_feast - steak, peppers, cheese
- veggie - tomamto, spinach, mushroom, eggs
