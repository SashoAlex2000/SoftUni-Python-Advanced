
size = 8
matrix = [input().split() for row in range(size)]

# for row in matrix:
#     print(row)

total_mating_queens = 0
list_of_mating_queens = []


def find_all_queens(queen_matrix):
    total_queens = 0
    for row in range(size):
        for col in range(size):
            if queen_matrix[row][col] == "Q":
                total_queens += 1

    return total_queens


count_of_queens = find_all_queens(matrix)


def find_queen(queen_matrix):
    for row in range(size):
        for col in range(size):
            if queen_matrix[row][col] == "Q":
                return row,col

def check_for_mate(queen_row,queen_col, matrix):
    #up
    for turn in range(queen_row-1,-1,-1):
        if matrix[turn][queen_col] == "Q" or matrix[turn][queen_col] == "O":
            break
        elif matrix[turn][queen_col] == "K":
            return True

    #down
    for turn in range(queen_row+1,size):
        if matrix[turn][queen_col] == "Q" or matrix[turn][queen_col] == "O":
            break
        elif matrix[turn][queen_col] == "K":
            return True

    #right
    for turn in range(queen_col+1,size):
        if matrix[queen_row][turn] == "Q" or matrix[queen_row][turn] == "O":
            break
        elif matrix[queen_row][turn] == "K":
            return True

    for turn in range(queen_col-1, -1, -1):
        if matrix[queen_row][turn] == "Q" or matrix[queen_row][turn] == "O":
            break
        elif matrix[queen_row][turn] == "K":
            return True

    reworked_row, reworked_col = queen_row, queen_col
    #right down diagonal
    while True:
        if reworked_row + 1 >= size or reworked_col + 1 >= size:
            break
        reworked_row += 1
        reworked_col += 1
        if matrix[reworked_row][reworked_col] == "K":
            return True
        elif matrix[reworked_row][reworked_col] == "Q" or matrix[reworked_row][reworked_col] == "O":
            break

    #left down diagonal
    reworked_row, reworked_col = queen_row, queen_col
    while True:
        if reworked_row + 1 >= size or reworked_col - 1 < 0:
            break
        reworked_row += 1
        reworked_col -= 1
        if matrix[reworked_row][reworked_col] == "K":
            return True
        elif matrix[reworked_row][reworked_col] == "Q" or matrix[reworked_row][reworked_col] == "O":
            break

    #right up diagonal
    reworked_row, reworked_col = queen_row, queen_col
    while True:
        if reworked_row - 1 < 0 or reworked_col + 1 >= size:
            break
        reworked_row -= 1
        reworked_col += 1
        if matrix[reworked_row][reworked_col] == "K":
            return True
        elif matrix[reworked_row][reworked_col] == "Q" or matrix[reworked_row][reworked_col] == "O":
            break
    #left up diagonal
    reworked_row, reworked_col = queen_row, queen_col
    while True:
        if reworked_row - 1 < 0 or reworked_col - 1 < 0:
            break
        reworked_row -= 1
        reworked_col -= 1
        if matrix[reworked_row][reworked_col] == "K":
            return True
        elif matrix[reworked_row][reworked_col] == "Q" or matrix[reworked_row][reworked_col] == "O":
            break

    return False


for turn in range(count_of_queens):
    current_queen_row,current_queen_col = find_queen(matrix)
    matrix[current_queen_row][current_queen_col] = "O"
    if check_for_mate(current_queen_row,current_queen_col,matrix):
        list_of_mating_queens.append([current_queen_row,current_queen_col])
        # print(f"{[current_queen_row,current_queen_col]}")
        total_mating_queens += 1

# print("!"*20)
# for row in matrix:
#     print(row)

if total_mating_queens == 0:
    print("The king is safe!")

# print(list_of_mating_queens)
for element in list_of_mating_queens:
    print(element)