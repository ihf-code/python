# 3. Create a Employee class and initialise it with name and staff number.
#  - i. Make methods to:
#  - display_info - It should display all the information of the employee.
#  - set_department - It should assign the department to employee.
#  - set_bonus - It should assign a bonus amount to the employee.

class Employee:
    def __init__(self, name, staff_number):
        self.name = name
        self.staff_number = staff_number

    def display_info(self):
        print("Employee Information: \n Name: " + self.name + "\n Staff ID: " + str(self.staff_number) + "\n Bonus: " + str(self.bonus) + "\n Department: " + str(self.department))

    def set_department(self, department):
        self.department = department

    def set_bonus(self, bonus):
        self.bonus = bonus


employee1 = Employee("Saf Mirza", 23435)
employee1.set_bonus(1000)
employee1.set_department("Technology")
employee1.display_info()

#  - ii. Create the instance attributes first name and last name instead of name.
#  - Create two methods full_name and email_address in the Employee class.
#  - Given a person's first and last names:
#  - Form the full_name method by simply joining the first and last name together, separated by a space.
#  - Form the email_address by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure everything is in lowercase.

class Employee:
    def __init__(self, first_name, last_name, staff_number):
        self.first_name = first_name
        self.last_name = last_name
        self.staff_number = staff_number

    def display_info(self):
        print(self.first_name, self.last_name, self.staff_number, self.bonus, self.department)

    def set_department(self, department):
        self.department = department

    def set_bonus(self, bonus):
        self.bonus = bonus

    def full_name(self):
        fullname = self.first_name + " " + self.last_name
        print("Fullname: " + fullname)

    def email_address(self):
        email = self.first_name + "." + self.last_name + "@company.com"
        print("Email: " + email.lower())


employee1 = Employee("Saf", "Mirza", 23435)
employee1.full_name()
employee1.email_address()
