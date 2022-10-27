

number_of_rows, number_of_columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(number_of_rows)]

max_sum = 0
magic_row_index = -1
magic_column_index = -1


for row_turn in range(number_of_rows-2):
    for column_turn in range(number_of_columns - 2):
        first_rw_sum = matrix[row_turn][column_turn] + matrix[row_turn][column_turn+1] + matrix[row_turn][column_turn+2]
        secnd_rw_sum = matrix[row_turn+1][column_turn] + matrix[row_turn+1][column_turn+1] + matrix[row_turn+1][column_turn+2]
        third_rw_sum = matrix[row_turn+2][column_turn] + matrix[row_turn+2][column_turn+1] + matrix[row_turn+2][column_turn+2]
        current_sum = first_rw_sum + secnd_rw_sum + third_rw_sum

        if current_sum > max_sum:
            magic_row_index = row_turn
            magic_column_index = column_turn
            max_sum = current_sum


print(f"Sum = {max_sum}")


i = 0
for row in range(magic_row_index, magic_row_index+3):
    for number in range(magic_column_index, magic_column_index+3):
        i += 1
        if i % 3 != 0:
            print(matrix[row][number],end=" ")
        else:
            print(matrix[row][number])

# for row in range(magic_row_index, magic_row_index+3):
#     magic_matrix.append([])
#     for number in range(magic_column_index, magic_column_index+3):
#         magic_matrix[row].apend(matrix[row][number])

