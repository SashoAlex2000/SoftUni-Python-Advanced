
i, n = [int(x) for x in input().split(', ')]
meta_list = []
total_sum = 0

for turn in range(i):
    curr_list = list(map(int, input().split(', ')))
    total_sum += sum(curr_list)
    meta_list.append(curr_list)


print(total_sum)
print(meta_list)
