# B2 - Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt"

f = open("even.txt", "w")

for x in open("numbers.txt"):
    x = int(x)
    if x % 2 == 0:
        f.write(str(x) + "\n")

f.close()
