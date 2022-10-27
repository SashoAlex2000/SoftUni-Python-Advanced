

number_of_rows, number_of_columns = [int(x) for x in input().split(" ")]

matrix = [[] for row in range(number_of_rows)]

i = 0

for row in range(number_of_rows):
    for iteration in range(number_of_columns):
        row_letter = 97 + row
        column_letter = 97 + iteration + i
        string_to_add = f"{chr(row_letter)}" + f"{chr(column_letter)}" + f"{chr(row_letter)}"
        matrix[row].append(string_to_add)
    i += 1

for row in matrix:
    print(" ".join(row))