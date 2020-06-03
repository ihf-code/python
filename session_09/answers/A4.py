# A4 - Create a function that will accept any number of parameters and save
# them all to a file, each on a new line.

def save_data(*args):
    f = open("test.txt", "w")

    for arg in args:
        f.write(str(arg) + "\n")

save_data(1, 2, 3, 4, 5, 6, 7, 8, 9, "jake")
