import sys
from sys import maxsize

jobs_list = list(map(int, input().split(", ")))
magic_index = int(input())
total_cycles = 0
current_lowest = sys.maxsize

while True:
    current_lowest_index = 0
    for number in jobs_list:
        if number < current_lowest:
            current_lowest = number
            current_lowest_index = jobs_list.index(number)


    # print(current_lowest)
    total_cycles += current_lowest

    current_lowest = sys.maxsize

    if current_lowest_index == magic_index:
        break

    if current_lowest_index < magic_index:
        magic_index -= 1

    # print(current_lowest_index)


    jobs_list.pop(current_lowest_index)



    # print(total_cycles)
    # print(jobs_list)

    if len(jobs_list) == 0:
        break

print(total_cycles)