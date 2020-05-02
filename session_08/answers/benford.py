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
