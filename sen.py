import random

choice = ["rock", "paper", "sissours"]
computer_choice = random.choice(choice)

user_choice = input("Enter your choice (Rock, Paper or sissours): ").lower()

if computer_choice == user_choice:
    print("it's a tie your choice is {user_choice} and the computer choice is {computer_choice}")
    
elif user_choice == "rock" and computer_choice == "sissours" or user_choice =="paper" and computer_choice == "rock" or user_choice == "sissours" and computer_choice == "paper":
    print(f"Congratulation You Win! your choice is {user_choice} and the computer choice is {computer_choice}")

else:
    print(f"You lose! your choice is {user_choice} and the computer choice is {computer_choice}")











