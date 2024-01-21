def create_board():
    # Creates a 5x5 grid represented as a list of lists
    return [[" " for _ in range(5)] for _ in range(5)]

def print_board(board):
    # Prints the board to the console
    print("\n  0 1 2 3 4")
    for i, row in enumerate(board):
        print(f"{i} {'|'.join(row)}")
    print()

def get_player_names():
    # Gets and returns player names
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")
    return player1, player2

def valid_move(row, col, board):
    # Checks if a move is valid (within the board)
    return 0 <= row < 5 and 0 <= col < 5

def update_board(board, row, col, player, remove=False):
    # Updates the board with the player's move, or removes a mark if remove is True
    if remove:
        board[row][col] = " "
    else:
        board[row][col] = player

def switch_player(current_player, player1, player2):
    # Switches the current player
    return player2 if current_player == player1 else player1

def check_win(board, player):
    # Checks for a winning condition (five in a row, column, or diagonal)
    for i in range(5):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(5)]):
            return True
    if all([board[i][i] == player for i in range(5)]) or all([board[i][4-i] == player for i in range(5)]):
        return True
    return False

def check_draw(board):
    # Checks if the game is a draw (board is full and no winner)
    return all(all(cell != " " for cell in row) for row in board)

def replay_game():
    # Asks players if they want to play again and returns the response
    choice = input("Do you want to play again? (yes/no): ")
    return choice.lower() == 'yes'

def tic_tac_toe():
    # Main function to run the Tic Tac Toe game
    board = create_board()
    player1, player2 = get_player_names()
    current_player = player1
    scores = {player1: 0, player2: 0}  # Initialize scores

    while True:
        print_board(board)
        print(f"{current_player}'s turn. Enter your move (row column), or 'r' to remove a mark: ")
        move = input().split()
        
        # Handle mark removal
        if move[0].lower() == 'r':
            print("Enter the coordinates of the mark you want to remove (row column):")
            try:
                row, col = map(int, input().split())
                if valid_move(row, col, board) and board[row][col] != " ":
                    update_board(board, row, col, current_player, remove=True)
                else:
                    print("Invalid move or no mark to remove. Try again.")
                    continue
            except ValueError:
                print("Please enter numbers only. Try again.")
                continue
        else:
            try:
                row, col = map(int, move)
                if valid_move(row, col, board) and board[row][col] == " ":
                    update_board(board, row, col, 'X' if current_player == player1 else 'O')
                else:
                    print("Invalid move or cell is occupied. Try again.")
                    continue
            except ValueError:
                print("Please enter numbers only. Try again.")
                continue

        # Check for win or draw and update scores
        if check_win(board, 'X' if current_player == player1 else 'O'):
            print_board(board)
            print(f"{current_player} wins!")
            scores[current_player] += 1
            if not replay_game():
                break
            board = create_board()
            current_player = player1
            continue

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            if not replay_game():
                break
            board = create_board()
            current_player = player1
            continue

        # Switch to the other player
        current_player = switch_player(current_player, player1, player2)

    # Print final scores after the game ends
    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

# Call the function to start the game
tic_tac_toe()



