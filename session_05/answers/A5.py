#A5 - Add up all the numbers from 1 to 500 and print the answer

total = 0

for x in range(1, 501):
    total += x

print(total)


# Another way
total = 0
number = 1

while number <= 500:
    total = total + number
    number = number + 1

print(total)


# Another way
total = 0
number = 1

while True:
    total = total + number
    number = number + 1

    if number > 500:
        break

print(total)
