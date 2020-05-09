# B4 - Benford’s law states that the leading digits in a collection of data are probably going to be small. 
# For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). 
# Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. 
# Work out which of the files contains fake data.

for x in range(1,4):
    f = open("accounts_" + str(x) + ".txt", "r")
    count = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
    }

    for num in f:
        if num:
            count[num[0]] += 1

    print(x)
    for y in range(1,10):
        print(str(y) + " = " + str(count[str(y)]/100) + "%")
