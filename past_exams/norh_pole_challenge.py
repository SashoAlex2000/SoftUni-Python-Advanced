number_of_rows, number_of_columns = list(map(int, input().split(", ")))

matrix = [input().split(" ") for row in range(number_of_rows)]

christmas_decorations = 0
gifts_collectd = 0
cookies_collected = 0

everything_collected = False


def find_santa(santa_matrix):
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            if santa_matrix[row][col] == "Y":
                return [row, col]


def find_items(item_matrix):
    total_items = 0

    for row in range(number_of_rows):
        for col in range(number_of_columns):
            if item_matrix[row][col] == "D" or item_matrix[row][col] == "G" or item_matrix[row][col] == "C":
                total_items += 1

    return total_items


def take_a_step(step_direction, step_row, step_col, max_row, max_col):
    if step_direction == "right":
        if step_col < (max_col - 1):
            return step_row, step_col + 1
        else:
            return step_row, 0

    elif step_direction == "left":
        if step_col > 0:
            return step_row, step_col - 1
        else:
            return step_row, max_col - 1

    elif step_direction == "up":
        if step_row > 0:
            return step_row - 1, step_col
        else:
            return max_row - 1, step_col

    elif step_direction == "down":
        if step_row < (max_row - 1):
            return step_row + 1, step_col
        else:
            return 0, step_col


santa_row, santa_col = find_santa(matrix)

command = input()

while command != "End":
    cmd_list = command.split("-")

    direction = cmd_list[0]
    steps = int(cmd_list[1])

    for turn in range(0, steps):
        current_row, current_col = take_a_step(direction, santa_row, santa_col, number_of_rows, number_of_columns)

        if matrix[current_row][current_col] == "D":
            christmas_decorations += 1
        elif matrix[current_row][current_col] == "G":
            gifts_collectd += 1
        elif matrix[current_row][current_col] == "C":
            cookies_collected += 1

        matrix[santa_row][santa_col] = "x"
        matrix[current_row][current_col] = "Y"

        items_left = find_items(matrix)

        if items_left <= 0:
            everything_collected = True
            break

        santa_row, santa_col = current_row, current_col

    if everything_collected:
        break

    command = input()

if everything_collected:
    print(f"Merry Christmas!")

print("You've collected: ")

print(f"- {christmas_decorations} Christmas decorations")
print(f"- {gifts_collectd} Gifts")
print(f"- {cookies_collected} Cookies")

for row in matrix:
    print(f" ".join(row))

