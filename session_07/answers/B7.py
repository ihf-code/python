# B7. Write a function that return True if a string is a pallindrome and False if it is not.

def pallindrome(word):
    reverse_word = word[::-1]
    if word == reverse_word:
        print(True)
    else:
        print(False)

pallindrome("strognsgag")
pallindrome("abba")
