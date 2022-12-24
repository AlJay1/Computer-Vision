# AiCore Computer Vision project

The goal was to create a Rock Paper Scissors game where the user can interact with the webcam.

To play the game ensure you have a webcam available on your device, download the dependencies in ```requirements.txt``` and then run the ```camera_rps_final.py``` file.


## Milestone 1 - Create the computer vision system

With Teachable-Machine, a series of images were taken for 4 different classes to create an image model (rock, paper, scissors and nothing).
The model was trained with the batch size, epochs, and learning rate at their default values: 50, 16, and 0.001, respectively.
The images of each class were diversified with varying hand positions, and different positions on the camera in an effort to reduce the risk of overfitting.
The model was downloaded with tensorflow and then added to the repository.

The labels for each image class is saved in ``` labels.txt ```
And the data for the image model is stored in ```keras_model.h5```

## Milestone 2 - Install the dependencies

To ensure that the code could be easily reproduced on other devices and by other users, a virtual environment was set up to manage dependencies.
The necessary libraries were installed such as tensorflow, opencv-python  and stored in the ```requirements.txt``` file to allow others to install and run the code. 


## Milestone 3 - Create a Rock-Paper-Scissors Game
In the ```manual_rps.py``` file, and rock paper scissors game was created was created with the user typing in their choice.
The ```get_computer_choice``` function in the RPS class generates the computer choice with the random library.
In the ```get_user_choice``` function asks the user to input the an option, the game will not preceed until a valid option has been entered.
The user is determined in the ```get_winner``` function. All the different permutations are covered and returns the winner of the that round.
The game is replayed until the either the user or the computer wins 3 rounds unless the user decides to quit.

## Milestone 4 - Use the Camera to Play Rock-Paper-Scissors

In the ```camera_rps_final.py``` fine, it uses a lot of the same functions in ```manual_rps.py``` but the ```get_prediction``` function is used to get the user choice with the camera.
There is a countdown of 5 seconds in the ```countdown``` function to allow the user some time to prepare their choice.
If the camera cannot detect a valid choice, it asks the user to show his choice again.
An easy and a hard mode is also implemented. Easy mode is where the computer randomly selects a choice.
Hard mode is where the user chooses based on the likely user choice, and then returns a choice that is most likely to win.



Milestone 4
Combination of milestone 3 and 4. This allows the user to show their choice to the camera and it returns the winner.
There is an easy and hard mode where the computer does not randomly choose, and predicts based on the user choice.
