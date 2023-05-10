# Create a list of 9 empty strings representing the game board
board = ["", "", "", "", "", "", "", "", ""]

# Display the current state of the game board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Play a single turn of the game
def play_turn(player):
    position = int(input("Player " + player + ", choose a position (1-9): "))
    # Check if the chosen position is valid and available
    while position < 1 or position > 9 or board[position-1] != "":
        position = int(input("Invalid position. Player " + player + ", choose an available position (1-9): "))
    # Update the game board with the player's move
    board[position-1] = player

# Check if the game has ended in a win, loss, or draw
def check_game_over():
    # Check for a win in rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "":
            return board[i]
    # Check for a win in columns
    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] != "":
            return board[i]
    # Check for a win in diagonals
    if board[0] == board[4] == board[8] != "" or board[2] == board[4] == board[6] != "":
        return board[4]
    # Check for a draw
    if "" not in board:
        return "draw"
    return False

# Play the game
def play_game():
    player = "X"
    while not check_game_over():
        display_board()
        play_turn(player)
        # Switch to the other player for the next turn
        if player == "X":
            player = "O"
        else:
            player = "X"
    display_board()
    # Determine the outcome of the game
    outcome = check_game_over()
    if outcome == "draw":
        print("It's a draw!")
    else:
        print("Player " + outcome + " wins!")
    # Ask if the players want to play again
    play_again = input("Do you want to play again? (y/n)").lower()
    while play_again != "y" and play_again != "n":
        play_again = input("Invalid input. Do you want to play again? (y/n)").lower()
    if play_again == "y":
        # Reset the game board and play again
        global board
        board = ["", "", "", "", "", "", "", "", ""]
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()
