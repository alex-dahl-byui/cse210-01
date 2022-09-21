# Tic-Tac-Toe - Alex Dahl

def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    winner = None
    player = 'x'
    while not winner:
        print_board(board)
        wanted_position = input(f"{player}'s turn to choose a square (1-9): ")
        print()
        horizontal_position = ""
        vertical_position = ""
        taken_positions = 0
        for horizontal_index, row in enumerate(board):
            for vertical_index, column in enumerate(row):
                if column == "x" or column == "o":
                    taken_positions += 1
                if wanted_position == column:
                    horizontal_position = horizontal_index
                    vertical_position = vertical_index
                    break

        board = update_board(board, horizontal_position, vertical_position, player)
        if taken_positions == 8:
            winner = "draw"
        else:
            winner = check_winner(board)
        if player == 'x':
            player = 'o'
        else:
            player = 'x'

    print_board(board)
    print(f'{winner} won')


def update_board(board, horizontal_position, vertical_position, player):
    new_board = board
    new_board[horizontal_position][vertical_position] = player
    return board


def print_board(board):
    for index, row in enumerate(board):
        print(" ".join(row))
        if index != len(board) - 1:
            print('-+-+-')
    print()


def check_winner(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]

    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]

    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]

    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]

    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]

    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


if __name__ == '__main__':
    main()
