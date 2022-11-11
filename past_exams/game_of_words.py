
initial_string = input()
size = int(input())

matrix = [list(input()) for row in range(size)]

# for row in matrix:
#     print(row)

number_of_turns = int(input())


def find_player_position(matrix_size ,player_matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            if player_matrix[row][col] == "P":
                return row, col


def check_for_punishment(direction, turn_matrix, row ,col):
    if direction == "right":
        if col +1 >= len(turn_matrix):
            return True
    elif direction == "left":
        if col - 1 < 0:
            return True
    elif direction == "down":
        if row + 1 >= len(turn_matrix):
            return True
    elif direction == "up":
        if row - 1 < 0:
            return True

    return False


def take_a_turn(direction, turn_matrix, row, col):
    if direction == "right":
        return row, col + 1
    if direction == "left":
        return row, player_col - 1
    if direction == "down":
        return player_row + 1, col
    if direction == "up":
        return player_row - 1, col


player_row, player_col = find_player_position(size, matrix)
#
# print(player_row)
# print(player_col)
valid_turns = 0

for turn in range(number_of_turns):
    direction = input()

    if check_for_punishment(direction, matrix, player_row, player_col):
        if len(initial_string) > 0:
            initial_string = initial_string[:-1]

    else:
        valid_turns += 1
        current_row, current_col = take_a_turn(direction, matrix, player_row, player_col)
        matrix[player_row][player_col] = "-"
        if matrix[current_row][current_col] == "-":
            player_row = current_row
            player_col = current_col

        else:
            initial_string = initial_string + matrix[current_row][current_col]
            matrix[current_row][current_col] = "-"
            player_row = current_row
            player_col = current_col

    # for row in matrix:
    #     print(row)
    # print("!!!!!!!!")

if valid_turns >= 1:
    player_row = current_row
    player_col = current_col
print(initial_string)
# noinspection PyUnboundLocalVariable
matrix[player_row][player_col] = "P"
for row in matrix:
    print("".join(row))


