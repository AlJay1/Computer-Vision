import random

rock_paper_scissors = ["rock", "paper", "scissors"]

def get_computer_choice():
    
    computer_choice = random.choice(rock_paper_scissors)
    return computer_choice

def get_user_choice():
    user_choice = input("Press r for rock, p for paper, s for scissors ")
    return user_choice


def get_winner(user_choice, computer_choice):

    if user_choice == "r":

        if computer_choice == "rock":
            print(f" The computer picked {computer_choice}, Draw")
        elif computer_choice == "scissors":
            print (f"The computer picked {computer_choice}, You win")
        else:
            print (f"The computer picked {computer_choice}, Computer wins")

    elif user_choice == "s":
        if computer_choice == "rock":
            print (f"The computer picked {computer_choice}, Computer wins")
        elif computer_choice == "scissors":
            print (f"The computer picked {computer_choice}, Draw")
        else:
            print (f"The computer picked {computer_choice}, You win")

    elif user_choice == "p":
        
        if computer_choice == "rock":
            print (f"The computer picked {computer_choice}, You wins")
        elif computer_choice == "scissors":
            print (f"The computer picked {computer_choice}, Computer wins")
        else:
            print (f"The computer picked {computer_choice}, Draw")

    else:
        print("Invalid input")



def play():
    get_winner(get_user_choice(), get_computer_choice())

play()