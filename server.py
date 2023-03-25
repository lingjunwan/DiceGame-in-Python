from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "softwareapplicationssecret"

WINNING_POINT = 20
final_score = 0

def roll_dice():
#Rolls the dice and returns a random integer between 1 and 6.
    return random.randint(1, 6)


@app.route('/', methods=['POST'])
def game():
#Starts a new game with the names of the two players and initializes the session variables.
    if request.method == 'POST':
        player1_name = request.form['player1_name']
        player2_name = request.form['player2_name']
        session['player1_name'] = player1_name
        session['player2_name'] = player2_name
        session['current_player'] = player1_name
        session['player1_score'] = 0
        session['player2_score'] = 0
        session['dice_value'] = 0

    return render_template('game.html', 
        player1_name=session['player1_name'],
        player2_name=session['player2_name'],
        player1_score=session['player1_score'],
        player2_score=session['player2_score'],
        current_player=session['current_player'],
        dice_value=session['dice_value'])


@app.route('/roll_dice', methods=['POST'])
def Roll_Dice_function():
#Handles the logic when the dice is rolled.
    dice_value = roll_dice()
    session['dice_value'] = dice_value

# logic for when the dice value is 1
    if dice_value == 1:
        if session['current_player'] == session['player1_name']:
            session['player1_score'] = 0 #reset player1's score
            session['current_player'] = session['player2_name'] #swap the player
        else:
            session['player2_score'] = 0 #reset player2's score
            session['current_player'] = session['player1_name'] #swap the player
    else:

# logic for when the dice value is not 1 
        if session['current_player'] == session['player1_name']:
            session['player1_score'] += dice_value
        else:
            session['player2_score'] += dice_value

# logic for when a player reaches the winning point
# If player 1 has won
    if session['player1_score'] >= WINNING_POINT:
        session['final_score'] = session['player1_score']
        return render_template('winner.html', winner=session['player1_name'], final_score = session['player1_score'])
# If player 2 has won
    elif session['player2_score'] >= WINNING_POINT:
        session['final_score'] = session['player2_score']
        return render_template('winner.html', winner=session['player2_name'], final_score = session['player2_score'])
    else:
# neither player has won yet        
        return render_template('game.html', 
        player1_name=session['player1_name'],
        player2_name=session['player2_name'],
        player1_score=session['player1_score'],
        player2_score=session['player2_score'],
        current_player=session['current_player'],
        dice_value=dice_value)


@app.route('/hold', methods=['POST'])
def hold():
#Handles the logic when the current player holds the dice.
    if session['current_player'] == session['player1_name']:
        session['current_player'] = session['player2_name']
    else:
        session['current_player'] = session['player1_name']

    return render_template('game.html', 
        player1_name=session['player1_name'],
        player2_name=session['player2_name'],
        player1_score=session['player1_score'],
        player2_score=session['player2_score'],
        current_player=session['current_player'],
        dice_value=session['dice_value'])


@app.route('/')
def logout():
#Clearing the session data and rendering the home page of the game.
    session.clear()
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)