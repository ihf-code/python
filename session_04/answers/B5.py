# B5 - 5. Create a list of ten random numbers.
# Loop through your list and count the number of even numbers and the number of odd numbers.

numbers = [1, 10, 13 , 15, 765, 32, 65, 23, 56, 101]
even_count = 0
odd_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        # This is short hand for the line above
        odd_count += 1

print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers.")
