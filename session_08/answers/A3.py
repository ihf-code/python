# A3 - Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file
total = 0
for x in open("numbers.txt"):
    total += int(x)
print(total)
