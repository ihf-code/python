#B8 - Create a list of 5 numbers. Write a for loop which appends the
# square of each number to the new list

numbers = [2, 5, 8, 9, 10]
sqr_numbers = []

for i in numbers:
    sqr_numbers.append(i ** 2)

print(sqr_numbers)
