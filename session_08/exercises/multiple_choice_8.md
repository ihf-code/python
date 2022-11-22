# KPMG:Code - Session 8 - Multiple Choice Questions

1. To open the below file, fill in the missing word:
f = ?("my_file.txt", "r")
- input
- read
- open - A
- close

2. To read the below file, fill in the missing word:
f = open("my_file.txt", "r")
print(f.?())
- input
- read - A
- open
- close

3. What does the "a" mode stand for? 
- read
- append - A 
- write
- create

4. "w" mode, overwrites the contents of your file.
- True - A 
- False

5. "a" mode, overwrites the contents of your file.

- True 
- False - A 

6. "r" mode will fail if the file its passed to doesn't exist.

- True - A 
- False 

7. To close the below file, fill in the missing word:
f = open("example.txt", "w")
f.write("Hello World")
f.?()

- input
- read
- open
- close - A 

8. To create a new file, file in the missing mode:
f = open("example.txt", "?")

- x - A 
- c
- r
- s 

9. What will be the output of the below:

total = 0
for x in open("example.txt"):
    total += 1

print(total)

- all the text from the file will be output 
- all the lines will be print out 
- the amount of lines in the file will be printed out - A 
- a new file will be created 

10. What will be the output of the below: 
f = open("odd.txt", "w")

for x in open("numbers.txt"):
    x = int(x)
    if x % 2 == 1:
        f.write(str(x) + "\n")

f.close()

- all the even numbers will be written to numbers.txt
- all the odd numbers will be written to numbers.txt
- all the even numbers will be written to even.txt 
- all the odd numbers will be written to odd.txt - A