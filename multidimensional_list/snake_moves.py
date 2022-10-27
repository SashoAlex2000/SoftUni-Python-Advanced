
number_of_rows, number_of_column = [int(x) for x in input().split(" ")]
word = input()

matrix = [["-" for x in range(number_of_column)] for row in range(number_of_rows)]
counter = 0
row_counter = 1

for row in range(number_of_rows):
    if row_counter % 2 != 0:
        for position in range(number_of_column):
            current_letter = word[counter]
            matrix[row][position] = current_letter
            counter += 1
            if counter >= len(word):
                counter = 0
        if counter >= len(word):
            counter = 0
    else:
        for position in range(number_of_column):
            current_letter = word[counter]
            matrix[row][-(position+1)] = current_letter
            counter += 1
            if counter >= len(word):
                counter = 0
        if counter >= len(word):
            counter = 0

    row_counter += 1

for row in matrix:
    print("".join(row))
