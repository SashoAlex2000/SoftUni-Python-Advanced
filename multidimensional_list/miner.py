def find_starting(curr_matrix):
    for row in range(len(curr_matrix)):
        for col in range(len(curr_matrix)):
            if curr_matrix[row][col] == "s":
                return [row, col]


def right_turn(matrixx, curr_position):
    roww = curr_position[0]
    coll = curr_position[1]

    if (coll + 1) < len(matrixx):
        new_position = [roww, coll + 1]
        return new_position
    return [roww, coll]


def left_turn(matrixx, curr_position):
    roww = curr_position[0]
    coll = curr_position[1]

    if (coll - 1) >= 0:
        new_position = [roww, coll - 1]
        return new_position
    return [roww, coll]


def up_turn(matrixx, curr_position):
    roww = curr_position[0]
    coll = curr_position[1]

    if (roww - 1) >= 0:
        new_position = [roww - 1, coll]
        return new_position
    return [roww, coll]

def down_turn(matrixx, curr_position):
    roww = curr_position[0]
    coll = curr_position[1]

    if (roww + 1) < len(matrixx):
        new_position = [roww + 1, coll]
        return new_position
    return [roww][coll]

def find_coal(coal_matrix):
    total_coal = 0
    for row in range(len(coal_matrix)):
        for col in range(len(coal_matrix)):
            if coal_matrix[row][col] == "c":
                total_coal += 1
    return total_coal


collected_coal = 0
premature_ending = False
number_of_rows = int(input())

commands = input().split()

matrix = [input().split() for row in range(number_of_rows)]

starting_position = find_starting(matrix)

for current_command in commands:

    if current_command == "right":
        new_position = right_turn(matrix, starting_position)

    elif current_command == "left":
        new_position = left_turn(matrix, starting_position)
    elif current_command == "up":
        new_position = up_turn(matrix, starting_position)
    elif current_command == "down":
        new_position = down_turn(matrix, starting_position)

    if new_position != starting_position:
        new_row = new_position[0]
        new_col = new_position[1]
        if matrix[new_row][new_col] == "c":
            collected_coal += 1
            matrix[new_row][new_col] = "*"
        elif matrix[new_row][new_col] == "e":
            premature_ending = True
        starting_position = new_position
    else:
        pass

    # for rw in matrix:
    #     print(rw)
    # print("!" * 10)
    # print(starting_position)
    # print("!" * 10)
    # if premature_ending:
    #     break

gmover_row = starting_position[0]
gmover_col = starting_position[1]
if premature_ending:

    print(f"Game over! ({gmover_row}, {gmover_col})")

else:
    coal_left = find_coal(matrix)

    if coal_left > 0:
        print(f"{coal_left} pieces of coal left. ({gmover_row}, {gmover_col})")
    else:
        print(f"You collected all coal! ({gmover_row}, {gmover_col})")