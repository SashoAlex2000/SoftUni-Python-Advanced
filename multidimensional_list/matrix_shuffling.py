number_of_rows, number_of_column = [int(x) for x in input().split(" ")]

matrix = [[x for x in input().split(" ")] for row in range(number_of_rows)]

line = input()

while line != "END":
    line_list = line.split(" ")
    command = line_list[0]
    is_valid = True

    if len(line_list) != 5:
        is_valid = False


    if command == "swap":
        row1 = int(line_list[1])
        col1 = int(line_list[2])
        row2 = int(line_list[3])
        col2 = int(line_list[4])

        if row1 > number_of_rows or row1 < 0:
            is_valid = False
        if row2 > number_of_rows or row2 < 0:
            is_valid = False
        if col1 > number_of_column or col1 < 0:
            is_valid = False
        if col1 > number_of_column or col1 < 0:
            is_valid = False

    else:
        is_valid = False

    if is_valid:
        number1 = matrix[row1][col1]
        number2 = matrix[row2][col2]

        matrix[row1][col1] = number2
        matrix[row2][col2] = number1

        for row in matrix:
            print(" ".join(row))
    else:
        print("Invalid input!")

    line = input()
