# A2 - Read the file 'austen.txt' and print the amount of lines in the file

#Option 1
total = 0
for x in open("austen.txt"):
    total += 1

print(total)

#Option 2 
f = open("austen.txt", "r")
count = 0
for x in f:
  count += 1

print(count)
