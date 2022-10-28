def find_santa(santa_matrix):
    for row in range(len(santa_matrix)):
        for col in range(len(santa_matrix)):
            if santa_matrix[row][col] == "S":
                return row, col


def count_good_kids(kid_matrix):
    total_good_kids = 0
    for row in range(len(kid_matrix)):
        for col in range(len(kid_matrix)):
            if kid_matrix[row][col] == "V":
                total_good_kids += 1
    return total_good_kids


def take_a_turn(row, col, direction):
    if direction == "right":
        return row, col + 1
    elif direction == "left":
        return row, col - 1
    elif direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col


def cookie_spread(cookie_matrix, row, col):
    cookie_presents = 0

    if cookie_matrix[row][col - 1] == "X" or cookie_matrix[row][col - 1] == "V":
        cookie_presents += 1
        cookie_matrix[row][col - 1] = "-"
    if cookie_matrix[row][col + 1] == "X" or cookie_matrix[row][col + 1] == "V":
        cookie_presents += 1
        cookie_matrix[row][col + 1] = "-"
    if cookie_matrix[row - 1][col] == "X" or cookie_matrix[row - 1][col] == "V":
        cookie_presents += 1
        cookie_matrix[row - 1][col] = "-"
    if cookie_matrix[row + 1][col] == "X" or cookie_matrix[row + 1][col] == "V":
        cookie_presents += 1
        cookie_matrix[row + 1][col] = "-"
    return cookie_presents


number_of_presents = int(input())
size = int(input())

matrix = [input().split() for row in range(size)]

santa_row, santa_col = find_santa(matrix)
total_good_kids = count_good_kids(matrix)
presents_delivered = 0
presents_are_over = False

line = input()

while line != "Christmas morning":

    current_row, current_col = take_a_turn(santa_row, santa_col, line)
    matrix[santa_row][santa_col] = "-"

    if matrix[current_row][current_col] == "-" or matrix[current_row][current_col] == "X":
        matrix[current_row][current_col] = "-"

    elif matrix[current_row][current_col] == "V":
        presents_delivered += 1
        matrix[current_row][current_col] = "-"
    elif matrix[current_row][current_col] == "C":
        curr_presents = cookie_spread(matrix, current_row, current_col)
        presents_delivered += curr_presents
        matrix[current_row][current_col] = "-"

    if presents_delivered >= number_of_presents:
        presents_are_over = True
    santa_row = current_row
    santa_col= current_col
    if presents_are_over:
        if count_good_kids(matrix) >= 1:
            print(f"Santa ran out of presents!")
        break


    line = input()

matrix[santa_row][santa_col] = "S"
for row in matrix:
    print(' '.join(row))


if presents_are_over:
    print(f"No presents for {count_good_kids(matrix)} nice kid/s.")
else:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")