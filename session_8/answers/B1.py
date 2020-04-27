# B1 - Write a function called is_odd that will return True if the integer is odd and
# False if the integer passed as a parameter is even (hint: x % 2 will return true for all odd numbers)


def is_odd(number):
    if number % 2 == 1:
        print(True)
    elif number % 2 == 0:
        print(False)
    else:
        print("")


is_odd(6)
is_odd(5)
