def find_player_position(player_matrix):
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            if player_matrix[row][col] == "P":
                player_position = [row, col]
                return player_position


def bunny_spread(bunny_matrix):
    initial_bunnies = []
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            if bunny_matrix[row][col] == "B":
                initial_bunnies.append([row, col])

    for pair in initial_bunnies:
        bunny_row = pair[0]
        bunny_col = pair[1]

        if (bunny_row - 1) >= 0:
            bunny_matrix[bunny_row - 1][bunny_col] = "B"
        if (bunny_col - 1) >= 0:
            bunny_matrix[bunny_row][bunny_col - 1] = "B"
        if (bunny_col + 1) < number_of_columns:
            bunny_matrix[bunny_row][bunny_col + 1] = "B"
        if (bunny_row + 1) < number_of_rows:
            bunny_matrix[bunny_row + 1][bunny_col] = "B"


number_of_rows, number_of_columns = [int(x) for x in input().split()]
matrix = [list(input()) for row in range(number_of_rows)]

command_list = list(input())
player_position = find_player_position(matrix)
has_exited = False
is_killed = False

for current_command in command_list:

    if current_command == "U":
        new_row = player_position[0] - 1
        if new_row < 0:
            has_exited = True
            matrix[player_position[0]][player_position[1]] = "."
        else:
            matrix[player_position[0]][player_position[1]] = "."
            player_position[0] = new_row

    elif current_command == "D":
        new_row = player_position[0] + 1
        if new_row > number_of_rows:
            has_exited = True
            matrix[player_position[0]][player_position[1]] = "."
        else:
            matrix[player_position[0]][player_position[1]] = "."
            player_position[0] = new_row
    elif current_command == "R":
        new_col = player_position[1] + 1
        if new_col > number_of_columns:
            has_exited = True
            matrix[player_position[0]][player_position[1]] = "."
        else:
            matrix[player_position[0]][player_position[1]] = "."
            player_position[1] = new_col
    elif current_command == "L":
        new_col = player_position[1] - 1
        if new_col < 0:
            matrix[player_position[0]][player_position[1]] = "."
            has_exited = True
        else:
            matrix[player_position[0]][player_position[1]] = "."
            player_position[1] = new_col

    player_row = player_position[0]
    player_col = player_position[1]

    if matrix[player_row][player_col] == "B":
        is_killed = True

    bunny_spread(matrix)
    if matrix[player_row][player_col] == "B":
        is_killed = True
    # for row in matrix:
    #     print(row)
    # print("!" * 10)

    if is_killed or has_exited:
        break

for row in matrix:
    print(''.join(row))

if has_exited:
    print(f"won: " + ' '.join(str(x) for x in player_position))
elif is_killed:
    print(f"dead: " + ' '.join(str(x) for x in player_position))

