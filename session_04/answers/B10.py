# B10 - FizzBuzz – Write a program that prints the numbers from 1 to 100.
# For multiples of three, print “Fizz” instead of the number and for multiples of five, print “Buzz”.
# For numbers which are multiples of both three and five, print “FizzBuzz”

# Example:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
