

number_of_rows = int(input())

matrix = [[int(x) for x in input().split(" ")] for row in range(number_of_rows)]

line = input()

while line != "END":
    line_list = line.split()
    command = line_list[0]
    # row = int(line_list[1])
    # col = int(line_list[2])
    # value = int(line_list[3])

    row, col, value = [int(x) for x in line_list[1:]]

    if 0 <= row <= (len(matrix) -1) and 0 <= col <= (len(matrix) -1):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value

    else:
        print(f"Invalid coordinates")
    line = input()

for row in matrix:
    print(' '.join(str(x) for x in row))
    # print(*row, sep=" ")