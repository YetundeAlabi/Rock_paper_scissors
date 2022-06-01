import random

options = ["R", "P", "S"]
shape = {"R": "Rock",
         "P": "Paper",
         "S": "Scissor"}


while True:
    user_choice = input('Pick an Option! "R", "P" or "S" ').upper()

    if user_choice not in options:
        print("Error! Invalid input.")
        continue

    computer_choice = random.choice(options)
    print(f"Player ({shape[user_choice]}): CPU ({shape[computer_choice]})")

    if user_choice == computer_choice:
        print("It's a Tie.")
        continue

    elif user_choice == "R" and computer_choice == "S"\
            or user_choice == "P" and computer_choice == "R"\
            or user_choice == "S" and computer_choice == "P":
        print("You win! Computer lose.")
        break

    else:
        print("You lost! Computer wins.")
        break



