# AiCore Computer Vision project

The goal was to create a Rock Paper Scissors game where the user can interact with the webcam.

To play the game, ensure you have a webcam available on your device, download the dependencies in ```requirements.txt``` and then run the ```camera_rps_final.py``` file.


## Milestone 1 - Create the computer vision system

With Teachable-Machine, a series of images were taken for 4 different classes to create an image model (rock, paper, scissors and nothing).
The model was trained with the batch size, epochs, and learning rate at their default values: 50, 16, and 0.001, respectively.
The images of each class were diversified with varying hand positions and positions on the camera to reduce the risk of overfitting.
The model was downloaded with TensorFlow and then added to the repository.

The labels for each image class are saved in ``` labels.txt ```
And the data for the image model is stored in ```keras_model.h5```

## Milestone 2 - Install the dependencies

A virtual environment was set up to manage dependencies and so that the code could be easily reproduced on other devices and by other users. 
The necessary libraries were installed, such as TensorFlow, opencv-python and stored in the ```requirements.txt``` file to allow others to install and run the code. 

## Milestone 3 - Create a Rock-Paper-Scissors Game
In the ```manual_rps.py``` file, a rock paper scissors game was created with the user typing in their choice.
The ```get_computer_choice``` function in the RPS class generates the computer choice with the random library.
The ```get_user_choice``` function asks the user to input an option. The game will not proceed until a valid option has been entered.
The user is determined in the ```get_winner``` function. All the different combinations are covered and returns the winner of that round.
The game is replayed until either the user or the computer wins 3 rounds unless the user decides to quit.

## Milestone 4 - Use the Camera to Play Rock-Paper-Scissors

In the ```camera_rps_final.py``` fine, it uses many of the same functions in ```manual_rps.py```, but the ```get_prediction``` function is used to get the user choice with the camera.
There is a countdown of 5 seconds in the ```countdown``` function to allow the user some time to prepare their choice.
If the camera cannot detect a valid choice, it asks the user to show his choice again.
An easy and a hard mode is also implemented. Easy mode is where the computer randomly selects a choice.
Hard mode is where the list of computer options is altered so that it is more likely to randomly choose the option that will beat the user's choice.
