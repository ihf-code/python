# A5 - Modify your previous answer to save key/value pairs in a file:
#    fname: Alice
#    lname: Smith
#    phone: 555-1234


def save_data(**kwargs):
    f = open("test.txt", "w")

    for key, value in kwargs.items():
        f.write(f"{key}: {value}\n")

save_data(fname = "Alice", lname = "Smith", phone = "555-1234")
