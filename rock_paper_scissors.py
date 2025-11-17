import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player_choice = None
    computer_choice = random.choice(options)

    while player_choice not in options:
        player_choice = input("Pick one! (rock, paper, scissors): ")

    print(f"Player's choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player wins!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins!")
    else:
        print("Player loses!")

    if not input("Do you want to play again? (y or n): ").lower() == "y":
        running = False