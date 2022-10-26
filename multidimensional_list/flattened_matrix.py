
number_of_lines = int(input())
matrix_list = []

for turn in range(number_of_lines):
    curr_list = [int(x) for x in input().split(", ")]
    # matrix_list.append([int(x) for x in input().split(", ")])
    for el in curr_list:
        matrix_list.append(el)

print(matrix_list)


