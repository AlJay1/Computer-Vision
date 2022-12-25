import cv2
import numpy as np
import random
import time
from keras.models import load_model

class RPS:

    '''
    This RPS class allows the user to play rock, paper, scissors by showing their choice to the camera.
    Attributes:
    user_options(list) = the options that the program detects from the user.
    comp_options(list)) = the options the computer can choose from.
    comp_wins(int) = the number of rounds the computer has won.
    user_wins(int) = the number of rounds the user has won
    max_score(int) - the number of rounds needed to win the game    
    '''

    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors", "Nothing"]
        self.user_choice = ""
        self.computer_choice = ""
        self.game_mode = ""
        self.comp_wins = 0
        self.user_wins = 0
        self.max_score = 3


    def get_computer_choice(self):
        '''
        In this method the computer randomly selects an option from self.comp_options.
        It returns the option as computer_choice.
        '''
        computer_choice = random.choice(self.options[0:3])
        #slices the nothing option out of the computer choice, only the user can pick nothing
        return computer_choice

    
    def get_prediction(self):
        '''
        This function allows the user to show an option to the computer by opening up the camera.
        Photos taken of the potential options and the data was stored in the file keras_model.h5.
        If the Nothing option is detected, it asks the user to try again.
        '''
        
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        timer = time.time() + 3
        #opens up the camra 3 seconds before the option is taken from the user.
        while timer > time.time(): 
            self.countdown()
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()
            user_choice = self.options[np.argmax(prediction)]
            #user choice is the highest probabilty out of self.options
            while user_choice == "Nothing":
                print("I did not catch that, can you try again")
                self.get_prediction()
                #if the camera detects nothing, it asks for the user to show their choice again.
            return user_choice


    def get_winner(self, user_choice, computer_choice):
        '''
        This function takes in the user and computer choices, and decides the winner of the round.        
        ''' 
        print(f"You picked {user_choice}, the computer picked {computer_choice},")
        #displays the user and computer options, and then decides the winner
        if user_choice == computer_choice:
            print ("Draw")

        #depending on who wins, either the computer or user wins is increased for each combination
        #the current score is displayed for the user to see
        elif user_choice == "Rock":
            if computer_choice == "Paper":
                self.comp_wins += 1
   
            else:
                self.user_wins += 1 
        
        elif user_choice == "Paper":
            if computer_choice == "Rock":
                self.user_wins += 1               

            elif computer_choice == "Scissors":
                self.comp_wins += 1               
                
        elif user_choice == "Scissors":
            if computer_choice == "Paper":
                self.user_wins += 1               
            
            elif computer_choice == "Rock":
                self.comp_wins += 1

        print (f"The score is {self.comp_wins} - {self.user_wins}")


    def replay(self):
        '''
        If either the computer or user has won 3 rounds, this function provides an option to play again
        '''
        replay = input("Press y if you want to play again ").lower()
        if replay == "y":
            #resets the computer and user wins to zero
            self.comp_wins = 0
            self.user_wins = 0
            self.play()
        else:
            #the user has decided to quit the game.
            exit()


    @staticmethod
    def countdown(): 
        '''
        This method prints out a countdown to the user which allows them time to prepare an option.  
        '''
        print("Show your hand in")
        t = 5
        #5 second timer
        while t != 0:
            minute, sec = divmod(t,60)
            timer = f"{sec}"
            cv2.waitKey(1000)
            print(f"{timer}...")
            #for each second it prints the remaining time to the user
            t-= 1


    def easy_mode(self):
        ''''
        This function plays the RPS game on easy mode.
        It calls the get_computer_choice and get_prediction function to get both the user and computer choices.
        It calls the get_winner function to decide the winner.
        Whoever reaches 3 wins first wins the game.
        '''

        computer_choice_easy = self.get_computer_choice()
        user_choice_easy = self.get_prediction()
        self.get_winner(user_choice_easy, computer_choice_easy)
        self.first_to_three()


    def hard_mode(self):
        '''
        This function is called hard mode.
        The computer does not randomly choose an option.
        It picks an option based on the prediction so that it is more likely to win
        '''
           
        user_choice_hard = self.get_prediction()
        #for each combination of user and computer choice, the computer choice option is appended by the winning option to increase the chance of the computer win
        #after it removes the added element so its a random choice the next time this function is called

        if user_choice_hard == "Rock":
            self.options.insert(0,"Paper")
            computer_choice_hard = random.choice(self.options[0:4])
            self.options.remove("Paper")          

        elif user_choice_hard == "Paper":
            self.options.insert(0,"Scissors")
            computer_choice_hard = random.choice(self.options[0:4])
            self.options.remove("Scissors")
          
        elif user_choice_hard == "Scissors":
            self.options.insert(0,"Rock")
            computer_choice_hard = random.choice(self.options[0:4])
            self.options.remove("Rock")           


        self.get_winner(user_choice_hard, computer_choice_hard)
        #calls the get winner function and passes in the 2 choices at arguments
        self.first_to_three()
        #calls the function to play the game 3 times


    def first_to_three(self):
        
        while True:
            #continues to play the game until either the computer or user has won
            if self.user_wins == 3:
                print ("You won the game!")
                self.replay()
                break
             
            elif self.comp_wins == 3:
                print( "The computer won")
                self.replay()
                break
            
            elif (self.game_mode == "e" and self.user_wins < 3) or  (self.comp_wins < 3 and self.game_mode == "e"):
                self.easy_mode()

            else:
                self.hard_mode()


    def play(self):
        '''
        This function plays the game, it allows the user to choose easy or hard mode.
        '''
        print(f"Welcome to Rock, Paper and Scissors! \nDo you want to play on easy mode or hard mode?")

        while True:
            game_mode = input("Press e for easy or h for hard ")
            
            if game_mode == "e":
                self.easy_mode()
                break
            elif game_mode == "h":
                self.hard_mode()
                break
            else:
                print ("Invalid input ")


if __name__ == "__main___":
    game = RPS()
    game.play()