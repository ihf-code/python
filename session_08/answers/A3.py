# A3 - Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file

#Option 1
total = 0
for x in open("numbers.txt"):
    total += int(x)

print(total)

#Option 2
f = open("numbers.txt", "r")
sum = 0 
for x in f:
  x = int(x)
  sum += x

print(sum)