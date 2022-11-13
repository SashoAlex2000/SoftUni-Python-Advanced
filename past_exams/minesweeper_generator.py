#START

size = int(input())
number_of_bombs = int(input())

matrix = [["-" for n in range(size)] for row in range(size)]

# for row in matrix:
#     print(row)

for turn in range(number_of_bombs):
    split_coords = input().split(", ")
    current_bomb_row = int(split_coords[0][1])
    current_bomb_col = int(split_coords[1][0])

    matrix[current_bomb_row][current_bomb_col] = "*"


def count_bombs(bomb_row,bomb_col, bomb_matrix,size):
    count_of_bombs_around = 0
    if bomb_col + 1 < size:
        if bomb_matrix[bomb_row][bomb_col+1] == "*":
            count_of_bombs_around += 1

    if bomb_col - 1 >= 0:
        if bomb_matrix[bomb_row][bomb_col-1] == "*":
            count_of_bombs_around += 1

    if bomb_row - 1 >= 0:
        if bomb_matrix[bomb_row-1][bomb_col] == "*":
            count_of_bombs_around += 1

    if bomb_row +1 < size:
        if bomb_matrix[bomb_row+1][bomb_col] == "*":
            count_of_bombs_around += 1

    #right_down diagonal
    if bomb_col +1 < size and bomb_row + 1 < size:
        if bomb_matrix[bomb_row + 1][bomb_col+1] == "*":
            count_of_bombs_around += 1

    #left down
    if bomb_col -1>= 0 and bomb_row + 1 < size:
        if bomb_matrix[bomb_row + 1][bomb_col - 1] == "*":
            count_of_bombs_around += 1

    # left up
    if bomb_col -1>= 0 and bomb_row - 1 >= 0:
        if bomb_matrix[bomb_row - 1][bomb_col - 1] == "*":
            count_of_bombs_around += 1

    #right up
    if bomb_col + 1 < size and bomb_row - 1 >= 0:
        if bomb_matrix[bomb_row - 1][bomb_col + 1] == "*":
            count_of_bombs_around += 1

    return count_of_bombs_around


# print("!"*10)
# for row in matrix:
#     print(row)

for row in range(size):
    for col in range(size):
        current_tile = matrix[row][col]

        if current_tile == "*":
            pass

        else:
            bombs_around = count_bombs(row,col,matrix,size)
            matrix[row][col] = bombs_around

#
# print("?"*10)
for row in matrix:
    print(" ".join([str(x) for x in row]))