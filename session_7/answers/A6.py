# A6 - Put the following into a function:
# i. If they are younger than 11, print "You're too young to go to this school"
# ii. If they are between 11 and 16, print "You can can come to this school"
# iii. If they are over 16, print 'You're too old for school"
# vi. If they are 0, print "You're not born yet!"


def school_eligibility(age):
    if age < 11:
        print("You're too young to go to this school.")
    elif age >= 11 and age <= 16:
        print("You can come to this school.")
    elif age > 16:
        print("You're too old for school.")
    elif age == 0:
        print("You're not born yet.")
    else:
        print("You didn't pick a number.")


school_eligibility(16)
school_eligibility(0)
school_eligibility(19)
