number_of_rows, number_of_columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for row in range(number_of_rows)]

identical_squares = 0

for row_turn in range(number_of_rows-1):
    for column_turn in range(number_of_columns - 1):
        first_symbol = matrix[row_turn][column_turn]
        second_symbol = matrix[row_turn][column_turn+1]
        third_symbol = matrix[row_turn+1][column_turn]
        fourth_symbol = matrix[row_turn+1][column_turn+1]

        if first_symbol == second_symbol == third_symbol == fourth_symbol:
            # print(f"SQUARE! : {first_symbol}")
            identical_squares += 1

print(identical_squares)