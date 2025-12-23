# import random

# # number = random.randint(100001,999999)

# # l = [45646466546,46464646462,646456465462,131634513164,4646461346]

# # print(random.choice(l))

# original = random.randint(1,50)

# print("*********** Enter Number between 1 to 50!!***********")

# while True:
#     Choice = int(input("Enter Choice :"))

#     if Choice>50:
#         print("Invalid Number ")
#         break

#     elif Choice==original:
#         print("Win!!!")
#         break 
#     elif Choice>original:
#         print("Choice is greater from the original number !!")
        
#     else:
#         print("Choice is smaller from the original number !!")

import random

Choices = ["rock", "paper", "scissors"]  # All valid choices included

while True:
    user_choice = input("Enter rock, paper or scissors: ").lower()  # Handle uppercase input
    computer_choice = random.choice(Choices)
    
    print("Computer chose:", computer_choice)  # Show computer's choice

    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors!")
            print("Rock Wins!")
        else:
            print("Paper covers rock!")
            print("You Lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cut paper!")
            print("Scissors Win!")
        else:
            print("Rock smashes scissors!")
            print("You Lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock!")
            print("Paper Wins!")
        else:
            print("Scissors cut paper!")
            print("You Lose!")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
