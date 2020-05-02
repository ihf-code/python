# A6 - Ask the user to enter the length and width of a shape and check if it is a square or not.

length = int(input("Please input the length:\n"))
width = int(input("Please input width:\n"))
if length == width:
  print("You are a square")
else:
  print("You are not a square")
