def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Rows, columns and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row,col): ")
            row, col = map(int, move.strip().split(","))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] not in ['X', 'O']:
                    return row, col
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Row and col must be 0, 1, or 2.")
        except:
            print("Invalid format. Enter as row,col (e.g., 0,2).")

def main():
    board = [['0', '1', '2'],
             ['3', '4', '5'],
             ['6', '7', '8']]

    # Initialize empty board with numbers
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("🎮 Tic-Tac-Toe Game")
    print("Players: X and O")
    print("Enter moves in row,col format (e.g., 0,1)")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_full(board):
            print("🤝 It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()

