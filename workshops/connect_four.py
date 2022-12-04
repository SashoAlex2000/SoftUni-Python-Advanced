# matrix
# print it

class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


# def check_row(rw, row_count):
#     if 0 <= rw < row_count:
#         return True
#     return False
#
#
# def check_col(cl, col_count):
#     if 0 <= cl < col_count:
#         return True
#     return False
#
#
# def check_winning_condition(mat, col_count, last_placed_row, last_placed_col, player_num):
#     row_count = len(mat)
#     has_won = False
#
# if check_col(last_placed_col+1,cols_count) and check_col(last_placed_col+2,cols_count) and check_col(
# last_placed_col+3, cols_count): if mat[last_placed_row][last_placed_col] == player_num and mat[last_placed_row][
# last_placed_col+1] == player_num and mat[last_placed_row][last_placed_col+2] == player_num and mat[
# last_placed_row][last_placed_col+3] == player_num: has_won = True

def is_player_num(ma, row, col, player_num, ):
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False


def is_horizontal(ma, row, col, player_num, slots_count):
    # count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    # count_left = [is_player_num(ma, row, col - index, player_num) for index in range(slots_count)].count(True)

    right_count = 0
    left_count = 0
    for turn in range(slots_count):
        if is_player_num(ma, row, col + turn, player_num) == False:
            break
        else:
            right_count += 1

    for turn in range(slots_count):
        if is_player_num(ma, row, col - turn, player_num) == False:
            break
        else:
            left_count += 1

    return (left_count + right_count) > slots_count


def is_right_diagonal(ma, row, col, player_num, slots_count):
    right_up_count = [is_player_num(ma, row - index, col + index, player_num) for index in range(slots_count)].count(
        True)
    left_down_count = [is_player_num(ma, row + index, col - index, player_num) for index in range(slots_count)].count(
        True)

    count_right_up = 0
    for turn in range(slots_count):
        if is_player_num(ma, row - turn, col + turn, player_num) == False:
            break
        else:
            count_right_up += 1
    count_left_down = 0
    for turn in range(slots_count):
        if is_player_num(ma, row + turn, col - turn, player_num) == False:
            break
        else:
            count_left_down += 1


    return (count_right_up + count_left_down) > 4


def is_left_diagonal(ma, row, col, player_num, slots_count):
    left_up_count = [is_player_num(ma, row - index, col - index, player_num) for index in range(slots_count)].count(
        True)
    right_down_count = [is_player_num(ma, row + index, col + index, player_num) for index in range(slots_count)].count(
        True)

    count_left_up = 0
    for turn in range(slots_count):
        if is_player_num(ma, row - turn, col - turn, player_num) == False:
            break
        else:
            count_left_up += 1

    count_right_down = 0
    for turn in range(slots_count):
        if is_player_num(ma, row + turn, col + turn, player_num) == False:
            break
        else:
            count_right_down += 1



    return (count_left_up + count_right_down) >= 5

    # TODO change variable names


def is_winner(ma, row, col, player_num, slots_count=4):
    is_horizontal(ma, row, col, player_num, slots_count)

    # is_right = all([is_player_num(ma, row, col + index, player_num) for index in range(slots_count)])
    # is_left = all([is_player_num(ma, row, col - index, player_num) for index in range(slots_count)])
    is_up = all([is_player_num(ma, row - index, col, player_num) for index in range(slots_count)])
    is_down = all([is_player_num(ma, row + index, col, player_num) for index in range(slots_count)])

    # is_right_up = all([is_player_num(ma, row - index, col + index, player_num) for index in range(slots_count)])
    # is_left_up = all([is_player_num(ma, row - index, col - index, player_num) for index in range(slots_count)])
    # is_right_down = all([is_player_num(ma, row + index, col + index, player_num) for index in range(slots_count)])
    # is_left_down = all([is_player_num(ma, row + index, col - index, player_num) for index in range(slots_count)])

    if any(
            [
                is_horizontal(ma, row, col, player_num, slots_count),
                is_up,
                is_down,
                is_right_diagonal(ma, row, col, player_num, slots_count),
                is_left_diagonal(ma, row, col, player_num, slots_count)
            ]
    ):
        return True
    return False


def print_matrix(matrix):
    for row in matrix:
        print(row)


def validate_column_choice(selected_col, max_col_index):
    if not 0 <= selected_col <= max_col_index:
        raise InvalidColumnError


def place_player_choice(ma, selected_col_index, player_num):
    rows_count = len(ma)

    for row_index in range(rows_count - 1, -1, -1):
        if ma[row_index][selected_col_index] == 0:
            ma[row_index][selected_col_index] = player_num
            return row_index, selected_col_index

    raise FullColumnError


rows_count = 6
cols_count = 7

matrix = [[0 for x in range(cols_count)] for row in range(rows_count)]

print_matrix(matrix)
player_num = 1

while True:
    try:
        column_num = int(input(f"Player {player_num}, please choose a column ")) - 1
        validate_column_choice(column_num, (cols_count - 1))
        row, col = place_player_choice(matrix, column_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print(f"The winner is player {player_num}")
            break
        print_matrix(matrix)


    except InvalidColumnError:
        print(f"This column is not valid. Please select a column between 1 and {cols_count}")
        continue
    except ValueError:
        print("please select a valid digit")
        continue
    except FullColumnError:
        print("This column is already full! Please select another column!")
        continue
    player_num += 1
    if player_num == 3:
        player_num = 1

print_matrix(matrix)
