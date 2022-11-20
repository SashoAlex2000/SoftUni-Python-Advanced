# START


size = 8

matrix = [input().split(" ") for row in range(size)]


# for row in matrix:
#     print(row)


def find_black_pawn(bl_matrix):
    for row in range(size):
        for col in range(size):
            if bl_matrix[row][col] == "b":
                return row, col


def find_white_pawn(wh_matrix):
    for row in range(size):
        for col in range(size):
            if wh_matrix[row][col] == "w":
                return row, col


def take_a_turn(color, row, col):
    if color == "white":
        return row - 1, col
    elif color == "black":
        return row + 1, col


def check_for_win(color, win_matrix, row, col):
    if color == "white":
        if 0 <= col - 1 < size:
            if win_matrix[row - 1][col - 1] == "b":
                return True

        if 0 <= col - 1 < size:
            if win_matrix[row - 1][col + 1] == "b":
                return True

    if color == "black":
        if 0 <= col - 1 < size:
            if win_matrix[row + 1][col - 1] == "w":
                return True

        if 0 <= col + 1 < size:
            if win_matrix[row + 1][col + 1] == "w":
                return True


row_dict = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}


def transform_coords(row, col):
    letter = chr(65 + col)
    number = row_dict[row]
    return letter, number


white_row, white_col = find_white_pawn(matrix)
black_row, black_col = find_black_pawn(matrix)
# print(white_row, white_col)
# print(black_row, black_col)

current_turn = 1
current_pawn = ""
capture_end = False
queen_promotion = False
white_won = False
black_won = False

while True:
    if current_turn % 2 != 0:
        current_pawn = "white"
    else:
        current_pawn = "black"

    if current_pawn == "white":
        current_row, current_col = find_white_pawn(matrix)
    elif current_pawn == "black":
        current_row, current_col = find_black_pawn(matrix)

    if check_for_win(current_pawn, matrix, current_row, current_col):
        capture_end = True
        if current_pawn == "white":
            white_won = True
        else:
            black_won = True

        # print(f"winning pawn is {current_pawn}")
        break

    new_row, new_col = take_a_turn(current_pawn, current_row, current_col)

    if current_pawn == "white":
        matrix[current_row][current_col] = "-"
        matrix[new_row][new_col] = "w"
    elif current_pawn == "black":
        matrix[current_row][current_col] = "-"
        matrix[new_row][new_col] = "b"

    if current_pawn == "white":
        if new_row == 0:
            # print("white became queen")
            queen_promotion = True
            white_won = True
            break

    if current_pawn == "black":
        if new_row == size - 1:
            # print("black became queen")
            queen_promotion = True
            black_won = True
            break

    current_turn += 1
    if current_turn == 3:
        current_turn = 1

    # for row in matrix:
    #     print(row)
    # print("!"*10)

# for row in matrix:
#     print(row)

if capture_end:
    if white_won:
        print_row, print_col = find_black_pawn(matrix)
        # print(f"{print_row} {print_col}")
        letter, number = transform_coords(print_row, print_col)
        letter = letter.lower()
        print(f"Game over! White win, capture on {letter}{number}.")
    elif black_won:
        print_row, print_col = find_white_pawn(matrix)
        # print(f"{print_row} {print_col}")
        letter, number = transform_coords(print_row, print_col)
        letter = letter.lower()
        print(f"Game over! Black win, capture on {letter}{number}.")

if queen_promotion:
    if white_won:
        print_row, print_col = find_white_pawn(matrix)
        letter, number = transform_coords(print_row, print_col)
        letter = letter.lower()

        print(f"Game over! White pawn is promoted to a queen at {letter}{number}.")
    elif black_won:
        print_row, print_col = find_black_pawn(matrix)
        letter, number = transform_coords(print_row, print_col)
        letter = letter.lower()
        print(f"Game over! Black pawn is promoted to a queen at {letter}{number}.")

# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - - - - - -
# - - - - - - - -
# - w - - - - - -
