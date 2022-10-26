
i, n = [int(x) for x in input().split(", ")]

matrix_list = [[int(x) for x in input().split(" ")] for row in range(i)]

# for row in matrix_list:
#     print(row)

for column in range(n):
    curr_sum = 0
    for rw in range(i):
        curr_sum += matrix_list[rw][column]
    print(curr_sum)
