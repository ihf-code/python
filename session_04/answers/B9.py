#B9 - Create a list with five names in. 
# Write a for loop which appends  Dr. to each name to the new list.

names = ["Saf", "Graham", "Jake", "Sanj", "Fis"]
drs = []
for name in names:
    drs.append("Dr. " + name)
print(drs)