# TOM AND JERRY

tom_jerry = input().split(", ")
size = 6

matrix = [input().split() for row in range(size)]

# for row in matrix: print(row)

first_player = tom_jerry[0]
second_player = tom_jerry[1]
first_skip = False
second_skip = False

counter = 1


while True:
    # tuple_input = tuple(input())
    # print(type(tuple_input))
    # print(tuple_input)
    shredded_input = input().split(", ")
    current_row = int(shredded_input[0][1])
    current_col = int(shredded_input[1][0])

    current_player = ""
    if counter == 1:
        current_player = first_player
        if first_skip:
            first_skip = False
            counter += 1
            if counter == 3:
                counter = 1
            continue
    if counter == 2:
        current_player = second_player
        if second_skip:
            second_skip = False
            counter += 1
            if counter == 3:
                counter = 1
            continue

    # print(f"{current_player} {current_row} {current_col}")
    if matrix[current_row][current_col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        if counter == 1:
            first_skip = True

        if counter == 2:
            second_skip = True
        # continue

    if matrix[current_row][current_col] == "T":
        print(f"{current_player} is out of the game! The winner is {first_player if current_player == second_player else second_player}.")
        break

    if matrix[current_row][current_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break


    counter += 1
    if counter == 3:
        counter = 1

# Jerry, Tom
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)
