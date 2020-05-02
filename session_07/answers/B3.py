# B3 - Write a recursive function that accepts a number and prints that number of stars,
# followed by ever decreasing stars on each line, E.g:
# *****
# ****
# **
# *


def print_stars(x):
    star = ""
    for y in range(0, x):
        star = star + "*"
    print(star)
    if x > 1:
        print_stars(x-1)


print_stars(10)
