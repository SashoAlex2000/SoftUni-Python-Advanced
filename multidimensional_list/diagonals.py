

number_of_lines = int(input())

matrix = [[int(x) for x in input().split(", ")] for row in range(number_of_lines)]
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

print(f"Primary diagonal: "+', '.join(str(x) for x in primary_list) + f". Sum: {primary_sum}")
print(f"Secondary diagonal: "+', '.join(str(x) for x in secondary_list) + f". Sum: {secondary_sum}")