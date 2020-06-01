## Section 9 Exercises

# Section A
1. Create a function that returns the first and last letters of the word passed in as separate variables.
2. Create a function that takes the circumferance of a circle and return the radius and area.
3. Create a function that takes a file name and word. Search the file to find all lines that start with the given word. Test your function using the file 'austen.txt' and find all lines that begin with "Mr". Hint: `.endswith("word")` is a function that returns True/False if a string ends with a value...maybe there is one that checks to see if a string "starts with"?
4. Create a function that will accept any number of parameters and save them all to a file, each on a new line.
5. Modify your previous answer to save key/value pairs in a file:
    fname: Alice
    lname: Smith
    phone: 555-1234
6. Create a function that can accept a series of numbers and a mathematical operand. Return the result of calculating the expression. E.g.:
    `calculate(1, 2, 3, 4, operand = "multiply")`
    `calculate(65, 200, 84, 12, operand = "add")`
7. Google the Python CSV library, and modify question 5 to save the data as a csv file. Make it so that you can enter as many contacts as you want and they each end up on a new row within the csv.
