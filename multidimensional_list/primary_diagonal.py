
number_of_lines = int(input())
matrix = [[int(x) for x in input().split()] for row in range(number_of_lines)]

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)

