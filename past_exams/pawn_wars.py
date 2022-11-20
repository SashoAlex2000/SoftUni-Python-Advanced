size = 8

matrix = [input().split(" ") for row in range(size)]


def find_black_pawn(black_matrix, black_size):
    for row in range(black_size):
        for col in range(black_size):
            if black_matrix[row][col] == "b":
                return [row, col]


def find_white_pawn(white_matrix, white_size):
    for row in range(white_size):
        for col in range(white_size):
            if white_matrix[row][col] == "w":
                return [row, col]


black_row, black_col = find_black_pawn(matrix, size)
white_row, white_col = find_white_pawn(matrix, size)


def take_a_turn(row, col, color):
    if color == "white":
        return [row - 1, col]
    elif color == "black":
        return [row + 1, col]

white_won = False
black_won = False

white_captured = False
black_captured = False

while True:

    current_white_row, current_white_col = take_a_turn(white_row,white_col, "white")

    if current_white_row == 0:
        white_won = True

    if (current_white_row - black_row == 1) and (current_white_col - black_col == 1 or black_col - current_white_col==1):
        white_captured = True

    # if (white_row - black_row == 1) and (white_col - black_col == 1 or black_col - white_col == 1):
    #     white_captured = True

    if white_won or white_captured:
        break

    current_black_row, current_black_col = take_a_turn(black_row,black_col, "black")

    if current_black_row == 7:
        black_won = True

    if (current_white_row - current_black_row == 1) and (current_white_col - current_black_col == 1 or current_black_col
                                                         - current_white_col == 1):
        black_captured = True

    if black_won or black_captured:
        break

    white_row = current_white_row
    white_col = current_white_col

    black_col = current_black_col
    black_row = current_black_row

if white_won:
    print(f"Game over! White pawn is promoted to a queen at {chr(97 + current_white_col)}8.")

if white_captured:
    print(f"Game over! White win, capture on {chr(97+black_col)}{8 - black_row}.")

if black_won:
    print(f"Game over! Black pawn is promoted to a queen at {chr(97 + current_black_col)}1.")

if black_captured:
    print(f"Game over! Black win, capture on {chr(97+current_white_row)}{8- current_white_col}.")


