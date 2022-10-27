

number_of_lines = int(input())

matrix = [[int(x) for x in input().split(" ")] for row in range(number_of_lines)]
primary_sum = 0
secondary_sum = 0

primary_list = []
secondary_list = []

for i in range(0, number_of_lines):
    primary_list.append(matrix[i][i])
    primary_sum += matrix[i][i]

for n in range(0, number_of_lines):
    secondary_list.append(matrix[n][-(n+1)])
    secondary_sum += matrix[n][-(n+1)]

absolute_difference = abs(primary_sum-secondary_sum)

primary_list = [str(x) if x >= 0 else f"({str(x)})" for x in primary_list]
secondary_list = [str(x) if x >= 0 else f"({str(x)})" for x in secondary_list]


# print(f"sum = " + ' + '.join(primary_list) + f' = {primary_sum}')
# print(f"sum = " + ' + '.join(secondary_list) + f' = {secondary_sum}')
#
# print(f"Difference: |{primary_sum} - {secondary_sum}| = {absolute_difference}")

print(absolute_difference)
