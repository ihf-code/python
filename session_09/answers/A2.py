# A2 - Read the file 'austen.txt' and print the amount of lines in the file
total = 0
for x in open("austen.txt"):
    total += 1
print(total)
