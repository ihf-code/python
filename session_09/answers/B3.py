# B3 - 'secret.txt' contains a secret message.
# Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26.
# Work out what the secret message says

alphabet = {
    0: "!",
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
}

word = ""
for x in open("secret.txt", "r"):
    x = int(x)
    word = word + alphabet[x]
print(word)
