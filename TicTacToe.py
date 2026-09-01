def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 9)
    print("\n")
def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)
def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player} enter your move as row,col (1-3 for each): ")
            row, col = map(int, move.split(','))
            if row not in [1, 2, 3] or col not in [1, 2, 3]:
                print("Row and column must be between 1 and 3.")
                continue
            if board[row - 1][col - 1] != ' ':
                print("That spot is already taken. Try again.")
                continue
            return row - 1, col - 1
        except ValueError:
            print("Invalid input format. Please enter row and column as numbers separated by a comma (e.g. 2,3).")
while True:
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")

    def print_board_inline():
        print("\n")
        for i in range(3):
            print(" | ".join(board[i]))
            if i < 2:
                print("-" * 9)
        print("\n")
    def check_win_inline(player):
        for i in range(3):
            if all(cell == player for cell in board[i]):
                return True
            if all(row[i] == player for row in board):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False
    def check_draw_inline():
        return all(cell != ' ' for row in board for cell in row)
    print_board_inline()
    while True:
        while True:
            try:
                move = input(f"Player {current_player} enter your move as row,col (1-3 for each): ")
                row, col = map(int, move.split(','))
                if row not in [1, 2, 3] or col not in [1, 2, 3]:
                    print("Row and column must be between 1 and 3.")
                    continue
                if board[row - 1][col - 1] != ' ':
                    print("That spot is already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input format. Please enter row and column as numbers separated by a comma (e.g. 2,3).")
        board[row - 1][col - 1] = current_player
        print_board_inline()

        if check_win_inline(current_player):
            print(f"Player {current_player} wins! 🎉")
            break
        if check_draw_inline():
            print("It's a draw! 🤝")
            break
        current_player = 'O' if current_player == 'X' else 'X'
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing Tic Tac Toe! Goodbye!")
        break
