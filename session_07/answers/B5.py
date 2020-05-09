# B5 - Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def multiples_3_and_5(limit):

    sum = 0
    
    for i in range (0, limit+1):
        if limit < 0:
            print("The limit must be greater than 0")
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    
    print(sum)

multiples_3_and_5(20)
    

