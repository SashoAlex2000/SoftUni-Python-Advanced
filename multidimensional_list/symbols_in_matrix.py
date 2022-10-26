
number_of_rows = int(input())

matrix = [list(input()) for row in range(number_of_rows)]
special_symbol = input()
has_occured = False

for row in range(number_of_rows):
    for item_in_column in range(number_of_rows):
        current_item = matrix[row][item_in_column]
        if current_item == special_symbol:
            has_occured = True
            special_tuple = (row, item_in_column)
        if has_occured:
            break
    if has_occured:
        break

if has_occured:
    print(special_tuple)
else:
    print(f"{special_symbol} does not occur in the matrix")


