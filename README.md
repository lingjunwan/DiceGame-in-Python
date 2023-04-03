# 🎲DiceGame in Python🎲


## Project Overview  
🎲The Dice Game is a web based two-player game where you accumulate points by rolling a dice. The first player to reach the winning point threshold (default 20) wins.  
  
🎲Enter the names of the two players to start the game. On your turn, click the "Roll Dice" button to roll the dice. Your score will increase by the value of the dice roll, but be careful - if you roll a 1, your score will be reset to 0, and your turn will end.  
  
🎲You can choose to "Hold" your score at any point during your turn, which will pass the turn to the other player. The game will continue until one player reaches the winning point threshold.   

## Preview  
>### home page:
![image](https://user-images.githubusercontent.com/118141976/229377170-630ebcab-de3d-4f9e-9f1d-4c017e48e8f9.png)  
The home.html template includes a form for the Player 1 and Player 2 to enter their names and a “Start Game” button to start the game.
It also provides the validation for empty input, regex validation requiring “Name must contain only letters and spaces, up to 20 characters” and a validation function to ensure that the two names are different. Also, the basic game rules are explained to provide a brief overview of the game and how to play it.

>### game page:
![image](https://user-images.githubusercontent.com/118141976/229377358-de626245-a8de-4194-a19e-7d3de92be807.png)  
After the Players input their names, by clicking the “Start Game” button, it will redirect us to the game.html template which includes the game board, with the players' names and scores, the dice picture, the tips for the game, the current player's name and the value of the dice rolled. Buttons for the players to “ROLL” the dice or “HOLD” their score is provided below the current player's name.  Also, an “EXIT” button on the top right corner of the page that allows the players to restart the game.

>### winner page:
![image](https://user-images.githubusercontent.com/118141976/229377718-79e6f2b2-f13b-47df-87b8-3cffc3cf0138.png)  
If one of the Player reaches 20 or more, the winner template will be displayed to show the Name of the player who wins and the Final Score of the Winner! Also, an “EXIT” button is available from here to restart the game.


## Features  
1. The application is built using `Flask` web framework and renders HTML templates using the `Jinja2` templating engine embedding `Bootstrap` `CSS` and `JavaScript`.  
2. The application uses `session` variables to store the current state of the game, including the names of the players, their scores, and the current player's turn.  
3. The game involves rolling a dice and adding the value of the dice to the current player's score.  
4. If the dice value is 1, the current player's score is reset to 0, and the turn is passed to the other player.  
5. The game continues until one player reaches a winning score of 20 points.  
6. The application includes two routes for rolling the dice and holding the dice and updating the scores and current player accordingly.  
7. The application also includes a logout route to clear the session data and start a new game.  
8. The application uses `PuTTY` Private Key (.ppk) file to connect to the `EC2 instance` and `WinSCP` for transferring files.  
9. The application is hosted on an AWS `EC2 instance` and a `Virtual Private Cloud (VPC)` is created to secure the instance.  
10. `TightVNC Viewer` is used to remotely control a `Ubuntu` desktop environment.  

## Instruction  
1. A Linux `Elastic Cloud Computer(EC2) instance` needs to be created and launched using `Amazon Web Service(AWS)` account.
2. Connect to the EC2 Instance from local computer using the `Secure Shell (SSH)` protocol.  
3. Create a `Virtual Private Cloud(VPC)` in AWS.  
4. Generate a PuTTY Private Key (.ppk) file using `PuTTY`, and connect to the EC2 instance.  
5. Transferring Files Using `WinSCP`.  
  
**Important:** Files must be transferred from your EC2 instance to your computer before you terminate the instance!  
When you transfer files, a copy of the files will be left on the instance. These will be deleted when the
instance is terminated.
