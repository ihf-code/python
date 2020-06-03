# A1 - Create a function that returns the first and last letters of the word
# passed in as separate variables.

# def first_last(word):
#    return (word[0], word[len(word) - 1])

def first_last(word):
    # 0 is the first index, -1 is the last
    return (word[0], word[-1])

# Unpack to 2 variables
first, last = first_last("python")

print(first, last)
