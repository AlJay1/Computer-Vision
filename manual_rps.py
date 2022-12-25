import random

class RPS:
    
    '''
    This RPS class allows the user to play rock, paper, scissors.
    Attributes:
    options(list) = the options available in the game
    comp_wins(int) = the number of rounds the computer has won.
    user_wins(int) = the number of rounds the user has won
    max_score(int) - the number of rounds needed to win the game    
    '''

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.comp_wins = 0
        self.user_wins = 0
        self.max_score = 3


    def get_computer_choice(self):
        '''
        Generates the computer choice of rock, paper or scissors using random module.
        '''
        computer_choice = random.choice(self.choices)
        return computer_choice


    def get_user_choice(self):
        '''
        Asks the user for a text input of their rock, paper, scissors choice and checks input validity.
        '''

        user_choice = input("Please choose one of rock, paper or scissors ").lower()
        #asks for user input
        while user_choice not in self.choices:
            #checks its a valid option
            user_choice = input("Invalid input, please choose one of rock, paper or scissors ").lower()
        return user_choice


    def get_winner(self, user_choice, computer_choice):
        '''
        Takes in the computer_choice and user_choice, and determined the winner of the game
        '''
        print(f"The computer picked {computer_choice}, you picked {user_choice}")

        if user_choice == computer_choice:
            print 
            print ("Draw")

        elif user_choice == "rock":
            if computer_choice == "paper":
                self.comp_wins += 1
                print("Computer wins")
            else:
                self.user_wins += 1 
                print ("You win!")

        elif user_choice == "paper":
            if computer_choice == "rock":
                self.user_wins += 1
                print ("You win!")

            elif computer_choice == "scissors":
                self.comp_wins += 1
                print("Computer wins")

        elif user_choice == "scissors":
            if computer_choice == "paper":
                self.user_wins += 1   
                print ("You win!")           
            
            elif computer_choice == "rock":
                self.comp_wins += 1
                print("Computer wins")

        print (f"The score is {self.comp_wins} - {self.user_wins}")


    def replay(self):
        '''
        Asks the user if they want to play again.
        '''

        replay = input("Press y if you want to play again ").lower()
        if replay == "y":
            self.comp_wins = 0
            self.user_wins = 0
            #resets user and computer wins to zero
            self.play()
        else:
            #the user has decided to quit the game.
            exit()


    def play(self):
        '''
        Calls all the functions in the correct order.
        '''
        comp = self.get_computer_choice()
        user = self.get_user_choice()
        self.get_winner(user, comp)

        while True:
            if self.user_wins == 3:
                print ("You won the game")
                self.replay()
                
            elif self.comp_wins == 3:
                print( "Computer won")
                self.replay()
            #calls the replay function to ask if the user wants to replay
            
            elif self.user_wins < 3 or  self.comp_wins < 3:
                self.play(self)
                #whilst either the user or computer has less than three wins, the game continues and the play function is called
           
if __name__ == "__main__":
    testing = RPS()
    testing.play()











