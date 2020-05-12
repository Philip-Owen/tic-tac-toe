# Game variables
winner = False

board = {
    "9": " ",
    "8": " ",
    "7": " ",
    "6": " ",
    "5": " ",
    "4": " ",
    "3": " ",
    "2": " ",
    "1": " ",
    "turns": 0,
}

winning_combinations = [
    "1,2,3",
    "4,5,6",
    "7,8,9",
    "1,4,7",
    "2,5,8",
    "3,6,9",
    "1,5,9",
    "3,5,7",
]
# End game variables


def check_winner(player):
    """
    Compare board dict to winning_combinations list to see if there is a match.
    Also checks if the game has ended in a tie and exits.
    """
    global winner
    for combo in winning_combinations:
        c = combo.split(",")

        if board[c[0]] is player and board[c[1]] is player and board[c[2]] is player:
            winner = True
            board_layout()
            print(f"\n*-*-*-*-*-*-*-*-* {player} wins *-*-*-*-*-*-*-*-*\n")

    if board["turns"] is 9 and winner is False:
        winner = True
        print(f"\n*-*-*-*-*-*-*-*-* cat's game *-*-*-*-*-*-*-*-*\n")


def board_layout():
    """
    Print the tic-tac-toe layout
    """
    print(
        f"""
    \u001b[2J\u001b[0;0H
    {board["7"]} | {board["8"]} | {board["9"]}
    ---------
    {board["4"]} | {board["5"]} | {board["6"]}
    ---------
    {board["1"]} | {board["2"]} | {board["3"]}
    """
    )


def print_choices():
    """
    Print the position choices
    """
    print(
        f"""
    7 | 8 | 9
    ---------
    4 | 5 | 6
    ---------
    1 | 2 | 3
    """
    )


def player_turn(player):
    """
    Receives input from the user, verifies input, verifies position is open and logs the players turn.
    Runs check_winner function at the end to see if a winning combination has been selected.
    """
    board_layout()
    print_choices()
    move = input(f"Player {player} choose a position number:")

    while int(move) > 9:
        board_layout()
        print_choices()
        print("\n***** Not a valid position number *****")
        move = input(f"Player {player} choose a position number:")

    if board[move] is not " ":
        while board[move] is not " ":
            board_layout()
            print_choices()
            print(
                "\n***** Position has already been selected, please select a new position *****"
            )
            move = input(f"Player {player} choose a position number:")

    board[move] = player
    board["turns"] += 1
    check_winner(player)


def play_game():
    """
    Runs the player_turn function for player X and player O. 
    Checks that winner variable is False before continuing the game.
    """
    if winner == False:
        player_turn("X")
    if winner == False:
        player_turn("O")


def tic_tac_toe():
    """
    Runs the play_game function while the winner variable.
    """
    while winner == False:
        play_game()


if __name__ == "__main__":
    tic_tac_toe()
