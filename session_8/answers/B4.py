# B4 - Create a padlock function.
# You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked"


def padlock(user_guess):

    pin = 8450
    if pin == user_guess:
        print("Unlock")
    else:
        print("Locked")


padlock(3423)
padlock(8450)
