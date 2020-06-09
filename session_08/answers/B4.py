# B4 - Benford’s law states that the leading digits in a collection of data are probably going to be small. 
# For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). 
# Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. 
# Work out which of the files contains fake data.

# STAGE 1 - this code allows us to check the values of one of the account files.
f = open("accounts_1.txt", "r")

count = {
  "0":0,
  "1":0,
  "2":0,
  "3":0,
  "4":0,
  "5":0,
  "6":0,
  "7":0,
  "8":0,
  "9":0
}

for x in f:
  if x:
    count[x[0]] += 1

for y in range(1,10):
  print(str(y) + " = " + str(count[str(y)]/100) + "%")

# STAGE 2 - Adding a for loop so we are able to loop through all accounts.
for x in range(1,4):
  f = open("accounts_" + str(x) + ".txt", "r")

  count = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
  }

  for num in f:
    if num:
      count[num[0]] += 1
  print(x)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

#STAGE 3 - Changing count so instead of us manually having to input count, it will create itself
for x in range(1,4):
  f = open("accounts_" + str(x) + ".txt", "r")

  count = {}
  for i in range(1,10):
    count[str(i)] = 0

  for num in f:
    if num:
      count[num[0]] += 1
  print(x)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

# STAGE 4 - Putting our code into a function - call 3 times

def benford_calc(file_name):
  f = open(file_name, "r")

  count = {}
  for i in range(1,10):
    count[str(i)] = 0

  for num in f:
    if num:
      count[num[0]] += 1
  print("Results for:" + file_name)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

benford_calc("accounts_1.txt")
benford_calc("accounts_2.txt")
benford_calc("accounts_3.txt")

# STAGE 5 - Looping through file names, so we don't need to call the function 3 times, as per stage 4
def benford_calc(file_name):
  f = open(file_name, "r")

  count = {}
  for i in range(1,10):
    count[str(i)] = 0

  for num in f:
    if num:
      count[num[0]] += 1
  print("Results for:" + file_name)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

for x in range (1,4):
  file_name = "accounts_" + str(x) + ".txt"
  benford_calc(file_name)

# STAGE 6 - Separating file function from data function 

def benford_calc_file(file_name):
  f = open(file_name, "r")
  return benford_calc(f)

def benford_calc(data):

  count = {}
  for x in range(1,10):
    count[str(x)] = 0

  for num in data:
      if num:
        count[str(num[0])] += 1
  
  return count 

for x in range (1,4):
  file_name = "accounts_" + str(x) + ".txt"
  data = benford_calc_file(file_name)

  print("Results for:" + file_name)

  for y in range(1,10):
      print(str(y) + " = " + str(data[str(y)]/100) + "%")

# STAGE 7 - Sending in a list of random numbers 

def benford_calc_file(file_name):
  f = open(file_name, "r")
  return benford_calc(f)

def benford_calc(data):

  count = {}
  for x in range(1,10):
    count[str(x)] = 0

  for num in data:
      if num:
        count[str(num[0])] += 1
  
  return count 

for x in range (1,4):
  file_name = "accounts_" + str(x) + ".txt"
  data = benford_calc_file(file_name)

  print("Results for:" + file_name)

  for y in range(1,10):
      print(str(y) + " = " + str(data[str(y)]/100) + "%")

random_nums = [str(random.randint(1,100)) for x in range(1,10001)]
data = benford_calc(random_nums)
print("Results for Random Nums")

for y in range(1,10):
      print(str(y) + " = " + str(data[str(y)]/100) + "%")