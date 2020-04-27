# Unexpected order of operations
sum = 4 + 5 * 2
print("4 + 5 * 2 = " + str(sum))

# Using brackets to define the order of operations you want
sum = (4 + 5) * 2
print("(4 + 5) * 2 = " + str(sum))

sum = 4 + 5 * 2 - 12 / 2 % 5
print("4 + 5 * 2 - 12 / 2 % 5 = " + str(sum))

sum = (4 + 5) * 2 - 12 / 2 % 5
print("(4 + 5) * 2 - 12 / 2 % 5 = " + str(sum))

sum = ((4 + 5) * 2 - 12 / 2) % 5
print("((4 + 5) * 2 - 12 / 2) % 5 = " + str(sum))

sum = (((4 + 5) * 2 - 12) / 2) % 5
print("(((4 + 5) * 2 - 12) / 2) % 5 = " + str(sum))

sum = ((((4 + 5) * 2) - 12) / 2) % 5
print("((((4 + 5) * 2) - 12) / 2) % 5 = " + str(sum))
