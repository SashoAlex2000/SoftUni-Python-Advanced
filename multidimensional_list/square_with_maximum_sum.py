
number_of_rows, number_of_columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for row in range(number_of_rows)]

# for row in matrix:
#     print(" ".join(str(x) for x in row))

magic_row_index = 0
magic_column_index = 0
max_sum = 0

for row in range(number_of_rows - 1):
    for column in range(number_of_columns - 1):
        current_sum = matrix[row][column] + matrix[row][column + 1] + matrix[row + 1][column] + matrix[row+1][column+1]
        # print(matrix[row][column])
        # print(matrix[row][column + 1])
        # print(matrix[row + 1][column])
        # print(matrix[row+1][column+1])
        # print(current_sum)
        # print("#"*10)
        if current_sum > max_sum:
            max_sum = current_sum
            magic_row_index = row
            magic_column_index = column
# print("!" * 20)

print(f"{matrix[magic_row_index][magic_column_index]} {matrix[magic_row_index][magic_column_index + 1]}")
print(f"{matrix[magic_row_index + 1][magic_column_index]} {matrix[magic_row_index + 1][magic_column_index + 1]}")
print(max_sum)