def find_rover(rover_matrix):
    for row in range(size):
        for col in range(size):
            if rover_matrix[row][col] == "E":
                return [row, col]


def take_a_turn(mars_matrix, row, col, direction):
    if direction == "right":
        if col == 5:
            return row, 0
        else:
            return [row, col + 1]

    elif direction == "left":
        if col == 0:
            return row, 5
        else:
            return [row, col - 1]

    elif direction == "up":
        if row == 0:
            return 5, col
        else:
            return [row - 1, col]

    elif direction == "down":
        if row == 5:
            return 0, col
        else:
            return [row + 1, col]


size = 6
matrix = [input().split(" ") for turn in range(size)]
commands = input().split(", ")
rover_row, rover_col = find_rover(matrix)

water_found = False
metal_found = False
concrete_found = False

rover_is_hit = False

for command in commands:

    current_row, current_col = take_a_turn(matrix, rover_row, rover_col, command)

    if matrix[current_row][current_col] == "-":
        pass
    elif matrix[current_row][current_col] == "W":
        water_found = True
        print(f"Water deposit found at ({current_row}, {current_col})")
    elif matrix[current_row][current_col] == "M":
        metal_found = True
        print(f"Metal deposit found at ({current_row}, {current_col})")
    elif matrix[current_row][current_col] == "C":
        concrete_found = True
        print(f"Concrete deposit found at ({current_row}, {current_col})")

    elif matrix[current_row][current_col] == "R":
        rover_is_hit = True
        print(f"Rover got broken at ({current_row}, {current_col})")

    rover_row = current_row
    rover_col = current_col

    if rover_is_hit:
        break

colony_is_suitable = False

if metal_found and concrete_found and water_found:
    colony_is_suitable = True

if colony_is_suitable:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
