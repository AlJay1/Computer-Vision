# AiCore Computer Vision project

The goal was to create a Rock Paper Scissors game where the user can interact with the webcam.


# Milestone 1 - Create the computer vision system

With Teachable-Machine, a series of images were taken for 4 different classes to create an image model (rock, paper, scissors and nothing).
The model was trained with the batch size, epochs, and learning rate at their default values: 50, 16, and 0.001, respectively.
The images of each class were diversified with varying hand positions, and different positions on the camera in an effort to reduce the risk of overfitting.
The model was downloaded with tensorflow and then added to the repository.

The labels for each image class is saved in '''labels.txt '''

# Milestone 2 - Install the dependencies

Images were taken of the rock, paper, scissors, and nothing options in teachable machine. 
And the model was downloaded.

Milestone 3
Conda environments was made and activated.
The libraries opencv, tensorflow, ipykernel and pip were installed.
The info regarding this can be found in requirements.txt

Milestone 4
RPS game was created with the user typing in their choice.
Using if/else statements, the winner was returned and the first to 3 round wins won the game.

Milestone 5
Combination of milestone 3 and 4. This allows the user to show their choice to the camera and it returns the winner.
There is an easy and hard mode where the computer does not randomly choose, and predicts based on the user choice.
