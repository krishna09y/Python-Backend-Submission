import random

Choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock,paper or scissors :").lower()
    computer_choice=random.choice(Choices)
    print("Computer chose:", computer_choice)
    if user_choice==computer_choice:
        print("tie")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("rock samsh scissors!")
            print("rock Win")
        
        else:
           print("Paper covers rock!")
           print("You Lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("scissors samsh paper!")
            print("scissors Win")
        else:
            print("Rock smashes scissors!")
            print("You Lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("paper samsh rock!")
            print("paper Win")
        else:
            print("Scissors cut paper!")
            print("You Lose!")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
    