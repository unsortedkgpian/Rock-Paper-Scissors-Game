import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors Or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock":
        if computer_pick == "rock":
            print("Tie")
            continue
        elif computer_pick == "paper":
            print("You Lose!")
            computer_wins += 1
            continue
        else:
            print("You won!")
            user_wins += 1
            continue
    if user_input == "paper":
        if computer_pick == "rock":
            print("You won!")
            user_wins += 1
            continue
        elif computer_pick == "paper":
            print("Tie")
            continue
        else:
            print("You Lose!")
            computer_wins += 1
            continue
    if user_input == "scissors":
        if computer_pick == "rock":
            print("You Lose")
            computer_wins += 1
            continue
        elif computer_pick == "paper":
            print("You win!")
            user_wins += 1
            continue
        else:
            print("Tie!")
            continue

print("You won", user_wins,"times.")
print("The computer won ", computer_wins, "times.")

print("Goodbye!")