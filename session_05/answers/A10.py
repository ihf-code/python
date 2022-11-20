# A10 - Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name

import random
prize_draw_list = []
user_input = None

# while the user does not enter a blank space, keep asking for names to be added to the draw
while user_input != "":
    user_input = input("Please input your name to be added to the prize draw:\n")
    # only if the user enters a name and not an empty string will it be added to the prize draw list
    if user_input != "":
        prize_draw_list.append(user_input)

# getting a random item out of the list and printing it as the winner 
print("Congratulations! " + random.choice(prize_draw_list) + " you are the winner of the prize draw!")