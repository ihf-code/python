# A11 - Rock, Paper, Scissors - Create a simple rock, paper, scissors game which is run against computer.

import random

print("Welcome to Rock, Paper, Scissors")

user_score = 0
computer_score = 0
turns = 0

while turns < 3:
  user_choice = input("What is your move? (rock, paper, scissors) ")
  computer_choice = random.choice(["rock", "paper", "scissors"])
  print("You picked " + user_choice)
  print("The computer picked " + computer_choice)
  turns += 1
  print("This is turn: " + str(turns))
  if user_choice == "rock":
      if computer_choice == "scissors":
          print("You Win")
          user_score += 1
      elif computer_choice == "paper":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")
  elif user_choice == "paper":
      if computer_choice == "rock":
          print("You Win")
          user_score += 1
      elif computer_choice == "scissors":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")
  else:
      if computer_choice == "paper":
          print("You Win")
          user_score += 1
      elif computer_choice == "rock":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")

print("Game Over! Final Score: User Score: " + str(user_score) + "\n Computer Score: " + str(computer_score)) 

  
  