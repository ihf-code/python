# B3 - The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
# If you roll a 6, you can draw the body
# If you roll a 5, you can draw the head
# If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
# If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
# If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
# If you roll a 1, you can draw the smile (but remember, you cannot draw a smile without a head)
# Create the beetle game.

import random
parts = {
    "1": "Eye",
    "2": "Mouth",
    "3": "Antennae",
    "4": "Leg",
    "5": "Head",
    "6": "Body"
}
beetles = []
scores = []

players = int(input("Please enter the number of players: "))

for x in range(players):
    beetles.append({
        "1": 2,  # eyes
        "2": 1,  # mouth
        "3": 2,  # antennae
        "4": 6,  # legs
        "5": 1,  # head
        "6": 1  # body
    })
    scores.append(0)

print("LETS START!!!!!")
winner = None

while not winner:
    for current_player in range(players):

        x = input("Player " + str(current_player) + ": Roll the dice...")
        if x == "q":
            break
        dice_roll = str(random.randint(1, 6))
        scores[current_player] += 1
        print("You rolled a: " + dice_roll)
        if beetles[current_player][dice_roll] > 0:
            if dice_roll == "1" and beetles[current_player]["5"]:
                print("Can't have an eye without a head")
            elif dice_roll == "2" and beetles[current_player]["5"]:
                print("Can't have a mouth without a head")
            elif dice_roll == "3" and beetles[current_player]["5"]:
                print("Can't have an antenna without a head")
            elif dice_roll == "4" and beetles[current_player]["6"]:
                print("Can't have a leg without a body")
            else:
                # valid roll therefore remove it from required go's
                print("You got a " + parts[dice_roll])
                beetles[current_player][dice_roll] -= 1
                for body_part in beetles[current_player]:
                    if beetles[current_player][body_part]:
                        print("You need " +
                              str(beetles[current_player][body_part]) + " " + parts[body_part])
                if sum(beetles[current_player].values()) == 0:
                    winner = current_player

print("The winner is: " + str(winner))

print(scores)
