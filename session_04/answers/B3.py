# B3 - Print all odd numbers from 1 to 100

# Loop through all 100 numbers and check each one to see if its odd
for i in range(1, 101):
    if i % 2:
        print(i)

# Use range to increment by 2 each time so 1, 3, 5 - happens to give you all odd numbers
for i in range(1, 101, 2):
    print(i)
