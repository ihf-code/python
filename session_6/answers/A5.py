# A5 - Rock, Paper, Scissors - Create a simple rock, paper, scissors game which is run against computer.

import random

print("\nWelcome to Rock, Paper, Scissors.\n You vs the Computer.\n Best of Three Wins\n")
computer_score = 0
user_score = 0
while computer_score < 3 and user_score < 3:
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(computer_choice)
    print(user_score)
    user_choice = input("Make your choice - rock, paper or scissors:\n")
    if user_choice == computer_choice:
        print("Draw")
        computer_score += 1
        user_score += 1
    elif user_choice == "rock" and computer_choice == "paper":
        print("You lose")
        computer_score += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lose")
        computer_score += 1
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lose")
        computer_score += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win")
        user_score += 1
    else:
        print("Please choose rock, paper or scissors")
        continue
print("Game Over")
