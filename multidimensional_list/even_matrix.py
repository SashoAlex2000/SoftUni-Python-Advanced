
i = int(input())
meta_list = []

for turn in range(i):
    curr_list = list(map(int, input().split(', ')))
    meta_list.append(curr_list)

# print(meta_list)
even_list = []

for row in meta_list:
    even_list.append([])
    for num in row:
        if num % 2 == 0:
            even_list[meta_list.index(row)].append(num)

print(even_list)