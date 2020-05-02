# B2 - Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'


def reverse_word(name):
    name_length = len(name)
    while name_length != 0:
        name_length -= 1
        print(name[name_length])


reverse_word("hello")
