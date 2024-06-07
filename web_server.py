# web_server.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
current_player = 0

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_full(board):
    return all([spot != " " for row in board for spot in row])

@app.route("/", methods=["GET", "POST"])
def index():
    global current_player, board

    if request.method == "POST":
        row = int(request.form["row"])
        col = int(request.form["col"])

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                winner = players[current_player]
                board = [[" " for _ in range(3)] for _ in range(3)]
                return render_template("index.html", board=board, message=f"Player {winner} wins!")
            elif check_full(board):
                board = [[" " for _ in range(3)] for _ in range(3)]
                return render_template("index.html", board=board, message="The game is a tie!")
            else:
                current_player = 1 - current_player

    return render_template("index.html", board=board)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
