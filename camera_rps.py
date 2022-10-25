import time
import cv2
from keras.models import load_model
import numpy as np
import random

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
        self.user_options = ["Rock", "Paper", "Scissors", "Nothing"]
        self.comp_options = ["Rock", "Paper", "Scissors"]
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
        
        random_index = random.randint(0, len(self.comp_options)-1)
        computer_choice = self.comp_options[random_index]
        return computer_choice

    
    def get_prediction(self):

        '''
        This function allows the user to show an option to the computer by opening up the camera.
        Photos taken of the potential options and the data was stored in the file keras_model.h5.
        If the Nothing option is detected, it asks the user to try again.
        
        '''

        import cv2
        from keras.models import load_model
        import numpy as np
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        timer = time.time() + 3

        while timer > time.time(): 
            RPS.countdown(self)
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
            user_choice = self.user_options[np.argmax(prediction)]
            while user_choice == "Nothing":
                print("I did not catch that, can you try again")
                RPS.get_prediction(self)
            return (user_choice)


    def get_winner(self, user_choice, computer_choice):

        '''
        This function takes in the user and computer choices, and decides the winner of the round.
        
        
        ''' 

        print(f"The computer picked {computer_choice}, you picked {user_choice}")

        if user_choice == computer_choice:
            print 
            print ("Draw")

        elif user_choice == "Rock":
            if computer_choice == "Paper":
                self.comp_wins += 1
                print(f"The score is {self.comp_wins} - {self.user_wins}")
                

            else:
                self.user_wins += 1 
                
                print (f"The score is {self.comp_wins} - {self.user_wins}")


        elif user_choice == "Paper":
            
            if computer_choice == "Rock":
                self.user_wins += 1

                
                print (f"The score is {self.comp_wins} - {self.user_wins}")

            elif computer_choice == "Scissors":
                self.comp_wins += 1

                
                
                print (f"The score is {self.comp_wins} - {self.user_wins}")


        elif user_choice == "Scissors":
            if computer_choice == "Paper":
                self.user_wins += 1

                
                print (f"The score is {self.comp_wins} - {self.user_wins}")
            
            elif computer_choice == "Rock":
                self.comp_wins += 1
                
                print (f"The score is {self.comp_wins} - {self.user_wins}")


    def replay(self):

        '''
        
        If either the computer or user has won 3 rounds, this function provides an option to play again
         
         '''


        replay = input("Press y if you want to play again ").lower()
        if replay == "y":
            self.comp_wins = 0
            self.user_wins = 0
            RPS.play(self)
        else:
            #the user has decided to quit the game.
            exit()

    def countdown(self): 


        '''
        This method prints out a countdown to the user which allows them time to prepare an option.  
        '''
        print("Show your hand in")
        t = 5
        while t != 0:
            minute, sec = divmod(t,60)
            timer = f"{sec}"
            cv2.waitKey(1000)
            print(f"{timer}...")
            t-= 1



    def easy_mode(self):

        ''''
        This function plays the RPS game on easy mode.
        It calls the get_computer_choice and get_prediction function to get both the user and computer choices.
        It calls the get_winner function to decide the winner.
        Whoever reaches 3 wins first wins the game.
        
        '''

        RPS.get_computer_choice()
        RPS.get_prediction()
        RPS.get_winner(self.user_choice, self.computer_choice)
        RPS.first_to_three()


    def hard_mode(self):
        '''
        This function is called hard mode.
        The computer does not randomly choose an option.
        It picks an option based on the prediction so that it is more likely to win
        
        '''
           
        RPS.get_prediction(self)

        if self.user_choice == "Rock":
            self.computer_choice = "Paper"
            return self.computer_choice

        elif self.user_choice == "Paper":
            self.computer_choice = "Scissors"
            return self.computer_choice

        else:
            self.computer_choice = "Rock"
            return self.computer_choice

        RPS.get_winner(self.user_choice, self.computer_choice)
        RPS.first_to_three()


    def first_to_three(self):

        while True:



            if self.user_wins == 3:
                print ("You won the game")
                RPS.replay(self)
                break
                        

             
            elif self.comp_wins == 3:
                print( "Computer won")
                RPS.replay(self)
                break
            


            elif self.user_wins < 3 or  self.comp_wins < 3 and self.game_mode == "e":
                RPS.easy_mode(self)

            else:
                RPS.hard_mode(self)


    def play(self):

        print("Welcome to Rock, Paper and Scissors /n Do you want to play on easy or hard mode? ")

        game_mode = input("Press e for easy or h for hard")

        while game_mode != "e" or "h":
            game_mode = input("I did not quite catch that, Press e for easy or h for hard")
        if game_mode == "e":
            RPS.easy_mode(self)

        else:
            RPS.hard_mode(self)

        




game = RPS().play()

