# A3 - Create a function that takes a file name and word. Search the file
# to find all lines that start with the given word. Test your function using
# the file 'austen.txt' and find all lines that begin with "Mr".
# Hint: `.endswith("word")` is a function that returns True/False if a string
# ends with a value...maybe there is one that checks to see if a
# string "starts with"?


def search_file(path, q):
    f = open(path, "r")

    # enumerate through the file
    for n, line in enumerate(f):
        # Check to make sure the line starts with your search term
        if line.startswith(q):
            print("Line: " + str(n + 1) + " - " + line)


search_file("austen.txt", "Mr")
