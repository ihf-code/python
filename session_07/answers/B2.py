# B2 - Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'


def reverse_word(name):
#METHOD 1 
    new_string = ""
    name_length = len(name)
    while name_length != 0:
        name_length -= 1
        new_string += name[name_length]
    return new_string

#METHOD 2
    # reverse = name[::-1]
    # print(reverse)



reverse_word("hello")
