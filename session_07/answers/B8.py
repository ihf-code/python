# B8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
# Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces. 

def pallindrome_sen(sentence):
    formatted_sen = sentence.lower()
    new_sentence = formatted_sen.replace(' ', '')
    rev_sentence = new_sentence[::-1]
    if new_sentence == rev_sentence:
        print(True)
    else:
        print(False)

pallindrome_sen("The cat sat on the mat")
pallindrome_sen("A nut for a jar of tuna")