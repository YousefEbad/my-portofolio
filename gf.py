import random

choice = input("Enter your choice Rock, Paper, sissours\n").lower()

choices = ["rock", "paper", "sissours"]


def game():
    computer_choice = random.choice(choices)

    if choice == computer_choice:
        print(f"It's a tie\nyou chose {choice} and the computer chose {computer_choice}")

    elif choice == "rock" and computer_choice =="paper" or choice == "paper" and computer_choice == "sissours" or choice == "sissours" and computer_choice == "paper":
        print(f"You win\nyou chose {choice} and the computer chose {computer_choice}")


    else:
        print(f"You lose\nyou chose {choice} and the computer chose {computer_choice}")
    

game()