# A6 - Create a blank list. 
# Ask a user input 10 numbers, 99 should be one of the numbers input. 
# Iterate through the list and print the index of number 99.

num_list = []
numbers = ""
i = 0
x = 0 
print("Pick 10 numbers, one of those numbers must be 99")

while i < 10:
  numbers = int(input("Pick a number:\n"))
  num_list.append(numbers)
  i += 1 

while x < len(num_list):
  if num_list[x] == 99:
    print("Number 99 is at index " + str(x))
  x += 1

  