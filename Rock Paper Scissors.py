import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors?: ").lower()

    if player == computer:
        print(f"Computer: {computer}")
        print(f"Player: {player}")
        print("Tie")

    elif player == "rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("Player lost :(")
        elif computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("Player won :)")

    elif player == "scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("Player lost :(")
        elif computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("Player won :)")

    elif player == "paper":
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("Player lost :(")
        elif computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("Player won :)")

    player_again = input("Want to play again (Yes or No)?: ").lower()

    if player_again != "yes":
        break

print("Bye!!!! Thank you for playing.")
