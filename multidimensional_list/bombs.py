# def explode_index(matrix, row, col, bomb):
#     if matrix[row][col] > 0 and row >= 0 and col >= 0:
#         matrix[row][col] -= bomb
#     else:
#         pass

def explode_index(matrix, row, col, bomb):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if matrix[row][col] > 0:
            matrix[row][col] -= bomb
    else:
        pass

def matrx_sum(curr_matrix):
    total_sum = 0
    living_cells = 0

    for row in range(len(curr_matrix)):
        for number in range(len(matrix)):
            if matrix[row][number] > 0:
                total_sum += matrix[row][number]
                living_cells += 1
    answer = [living_cells, total_sum]
    return answer


number_of_rows = int(input())

matrix = [[int(x) for x in input().split(" ")] for row in range(number_of_rows)]

bomb_list = []
bomb_initial = [bomb_set for bomb_set in input().split(" ")]

for bomb_set in bomb_initial:
    split_bombs = bomb_set.split(",")
    roww = int(split_bombs[0])
    col = int(split_bombs[1])
    bomb_set = (roww, col)
    bomb_list.append(bomb_set)



for turns in range(len(bomb_list)):
    current_explosion = bomb_list[turns]
    current_row = current_explosion[0]
    current_col = current_explosion[1]
    explosion_curr = matrix[current_row][current_col]

    if explosion_curr > 0:
        matrix[current_row][current_col] = 0
        explode_index(matrix, (current_row - 1), (current_col - 1), explosion_curr)
        explode_index(matrix, (current_row - 1), current_col, explosion_curr)
        explode_index(matrix, (current_row - 1), (current_col + 1), explosion_curr)
        explode_index(matrix, current_row, (current_col + 1), explosion_curr)
        explode_index(matrix, current_row, (current_col - 1), explosion_curr)
        explode_index(matrix, (current_row + 1), (current_col - 1), explosion_curr)
        explode_index(matrix, (current_row + 1), current_col, explosion_curr)
        explode_index(matrix, (current_row + 1), (current_col + 1), explosion_curr)


alive_cells, total_sum = matrx_sum(matrix)

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")

for row in matrix:
    print(" ".join(str(x) for x in row))