from math import floor

number_of_rows = int(input())
position_list = []

matrix = [input().split() for row in range(number_of_rows)]
collected_coins = 0


def find_player(pl_matrix, size):
    for row in range(size):
        for col in range(size):
            if pl_matrix[row][col] == "P":
                return row, col


def take_a_turn(row, col, direction, size):

    if direction == "right":
        if col < size -1:
            return row, col+1
        else:
            return row, 0

    elif direction == "left":
        if col > 0:
            return row, col - 1

        else:
            return row, size - 1
    elif direction == "up":
        if row > 0:
            return row - 1, col
        else:
            return size - 1, col

    elif direction == "down":
        if row < size - 1:
            return row + 1, col
        else:
            return 0, col

player_row, player_col = find_player(matrix, number_of_rows)
player_hit_a_wall = False

while True:
    curr_tuple = (player_row, player_col)
    position_list.append(curr_tuple)

    command = input()
    current_row, current_col = take_a_turn(player_row,player_col,command,number_of_rows)
    if matrix[current_row][current_col].isnumeric():
        collected_coins += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = "C"
    elif matrix[current_row][current_col] == "X":
        player_hit_a_wall = True

    player_row, player_col = current_row, current_col
    if player_hit_a_wall or collected_coins >=100:
        break

curr_tuple = (player_row, player_col)
position_list.append(curr_tuple)

if player_hit_a_wall:
    collected_coins = floor(collected_coins/2)

if player_hit_a_wall:
    print(f"Game over! You've collected {collected_coins} coins.")
else:
    print(f"You won! You've collected {collected_coins} coins.")

print("Your path:")
for double in position_list:
    print(f"[{double[0]}, {double[1]}]")