import random

your_choice = str(input("choose Rock / Paper / scissors: "))
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print(computer_choice)

if your_choice == computer_choice:
    print("game tie")
elif your_choice == "rock":
    if computer_choice == "paper":
        print("paper covers rock, you lose")
    else:
        print("rock smashes scissors, you win!")
elif your_choice == "paper":
    if computer_choice == "scissors":
        print("scissors cuts paper, you lose")
    else:
        print("paper covers rock, you win!")
elif your_choice == "scissors":
    if computer_choice == "rock":
        print("rock smashes scissors, you lose")
    else:
        print("scissors cuts paper, you win")
else:
    print("invalid entry")


