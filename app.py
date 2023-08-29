import random
from flask import Flask, render_template, request, session

# Create a Flask web application instance
app = Flask(__name__)

# Set a secret key for the session
app.secret_key = '0x45f4'

# Define a route for the root URL ('/')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/play", methods=["POST"])
def play():
    # Retrieve the value of the 'choice' form field from the POST request
    player_choice = request.form["choice"]

    if "count" not in session:
        session["count"] = 0

    
    choice_list = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choice_list)

    if ( (computer_choice == "rock" and player_choice == "scissor") or (computer_choice == "paper" and player_choice == "rock") 
        or (computer_choice == "scissor" and player_choice == "paper") ):
        result = "You lose 😭\n"
    elif computer_choice == player_choice:
        result = "It's a tie!"
    else:
        result = "You win 😍\n"
        session["count"] += 1

    # Render the 'result.html' template with relevant information
    return render_template('result.html', player=player_choice, computer=computer_choice, result=result,count=session["count"])

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
