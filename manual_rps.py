import random

class RPS:

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.comp_wins = 0
        self.user_wins = 0
        self.max_score = 3


    def get_computer_choice(self):
        
        random_index = random.randint(0, len(self.choices)-1)
        computer_choice = self.choices[random_index]
        return computer_choice

    def get_user_choice(self):
        user_choice = input("Please choose one of rock, paper or scissors ").lower()
        while user_choice not in self.choices:
            user_choice = input("Invalid input, please choose one of rock, paper or scissors ").lower()

        return user_choice


    def get_winner(self, user_choice, computer_choice):

        print(f"The computer picked {computer_choice}, you picked {user_choice}")

        if user_choice == computer_choice:
            print 
            print ("Draw")

        elif user_choice == "rock":
            if computer_choice == "paper":
                self.comp_wins += 1
                print(f"The score is {self.comp_wins} - {self.user_wins}")
                


            else:
                self.user_wins += 1 
                
                print (f"The score is {self.comp_wins} - {self.user_wins}")


        elif user_choice == "paper":
            
            if computer_choice == "rock":
                self.user_wins += 1

                
                print (f"The score is {self.comp_wins} - {self.user_wins}")

            elif computer_choice == "scissors":
                self.comp_wins += 1

                
                
                print (f"The score is {self.comp_wins} - {self.user_wins}")


        elif user_choice == "scissors":
            if computer_choice == "paper":
                self.user_wins += 1

                
                print (f"The score is {self.comp_wins} - {self.user_wins}")
            
            elif computer_choice == "rock":
                self.comp_wins += 1
                
                print (f"The score is {self.comp_wins} - {self.user_wins}")


    def replay(self):
        replay = input("Press y if you want to play again ").lower()
        if replay == "y":
            self.comp_wins = 0
            self.user_wins = 0
            RPS.play(self)
        else:
            #the user has decided to quit the game.
            exit()




    def play(self):
        comp = self.get_computer_choice()
        user = self.get_user_choice()

        self.get_winner(user, comp)

        while True:

            if self.user_wins == 3:
                print ("You won the game")
                RPS.replay(self)
                        

             
            elif self.comp_wins == 3:
                print( "Computer won")
                RPS.replay(self)
            


            elif self.user_wins < 3 or  self.comp_wins < 3:
                RPS.play(self)
           

game = RPS().play()










