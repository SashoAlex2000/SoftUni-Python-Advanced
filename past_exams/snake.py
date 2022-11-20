size = int(input())

matrix = [list(input()) for row in range(size)]
burrow_coords_dict = {}

def find_snake(snake_matrix):
    for row in range(size):
        for col in range(size):
            if snake_matrix[row][col] == "S":
                return row, col


def count_of_burrows(bur_matrix):
    total_burrows = 0
    for row in range(size):
        for col in range(size):
            if bur_matrix[row][col] == "B":
                total_burrows += 1

    return total_burrows


def find_burrows(burrow_matrix, bur_dict):

    for row in range(size):
        for col in range(size):
            if burrow_matrix[row][col] == "B":
                current_burrow = len(bur_dict) + 1
                bur_dict[current_burrow] = [row, col]

def take_a_turn(turn_matrix, direction, turn_row, turn_col):
    if direction == "right":
        return turn_row, turn_col + 1
    if direction == "left":
        return turn_row, turn_col - 1
    if direction == "down":
        return turn_row + 1, turn_col
    if direction == "up":
        return turn_row - 1, turn_col


total_burrows = count_of_burrows(matrix)

if total_burrows > 0:
    find_burrows(matrix,burrow_coords_dict)

food_is_collected = False
snake_row, snake_col = find_snake(matrix)
collected_food = 0
game_over = False
matrix[snake_row][snake_col] = "."

while True:
    command = input()
    current_row, current_col = take_a_turn(matrix, command, snake_row, snake_col)

    if current_row < 0 or current_row >= size or current_col < 0 or current_col >= size:
        game_over = True
        break

    if matrix[current_row][current_col] == "-" or matrix[current_row][current_col] == ".":
        pass
    elif matrix[current_row][current_col] == "*":
        collected_food += 1
    elif matrix[current_row][current_col] == "B":
        current_burrow = -100
        for bur,coords in burrow_coords_dict.items():
            if coords == [current_row, current_col]:
                current_burrow = bur
        matrix[current_row][current_col] = "."

        if current_burrow == 1:
            current_row = burrow_coords_dict[2][0]
            current_col = burrow_coords_dict[2][1]
        elif current_burrow == 2:
            current_row = burrow_coords_dict[1][0]
            current_col = burrow_coords_dict[1][1]

    if collected_food >= 10:
        food_is_collected = True
        break

    snake_row,snake_col = current_row, current_col
    matrix[snake_row][snake_col] = "."


if not game_over:
    matrix[current_row][current_col] = "S"

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {collected_food}")
for row in matrix:
    print("".join(row))



