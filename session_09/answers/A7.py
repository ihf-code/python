# A7 - Google the Python CSV library, and modify question 5 to save the
# data as a csv file. Make it so that you can enter as many contacts as
# you want and they each end up on a new row within the csv.

import csv

# def save_data(**kwargs):
#     f = open("test.txt", "a")
#     csvwriter = csv.writer(f)
#     csvwriter.writerow(kwargs.values())
#     f.close()
#
# save_data(fname = "Alice", lname = "Smith", phone = "555-1234")
# save_data(fname = "Bob", lname = "Smith", phone = "555-1234")
# save_data(fname = "Charlie", lname = "Smith")


fields = ["fname", "lname", "phone"]


w = csv.DictWriter(open("contacts.csv", "w"), fieldnames=fields)

w.writeheader()
w.writerow({"fname": "jake"})
w.writerow({"lname": "smith"})
