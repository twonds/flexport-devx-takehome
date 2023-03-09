import json


from flask import Flask, request

from rps import rock_paper_scissors


class InvalidMove(Exception):
    """
    Invalid Move
    """

app = Flask(__name__)


@app.route("/health")
def health():
    return "OK"

@app.route("/rps", methods = ['POST'])
def rps():
    # Create number to choice mapping
    mapping = ["Rock", "Paper", "Scissors"]

    move = request.json.get('move', '')
    try:
        user_choice = mapping.index(move.lower().capitalize())
    except ValueError:
        raise InvalidMove(f"{move} is invalid. Valid moves: {mapping}")

    game_result  = rock_paper_scissors(user_choice)
    if game_result == 0:
        result = "Tie"
    elif game_result == -1:
        result = f"I win, {mapping[pc_choice]} beats {move}"
    else:
        result = f"You win, {move} beats {mapping[pc_choice]}"

    return json.dumps({'result': result})
