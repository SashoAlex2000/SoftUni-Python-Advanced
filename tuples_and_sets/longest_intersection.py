
number_of_lines = int(input())
all_intersections = []

for turn in range(number_of_lines):
    current_pair_list = input().split("-")

    first_pair = [int(x) for x in current_pair_list[0].split(",")]
    first_set = set()
    for i in range(first_pair[0], first_pair[1]+1):
        first_set.add(i)

    second_pair = [int(x) for x in current_pair_list[1].split(",")]
    second_set = set()
    for i in range(second_pair[0], second_pair[1] + 1):
        second_set.add(i)

    current_intersection = first_set&second_set
    all_intersections.append(current_intersection)


max_length = -1
longest_set = ""

for inter_set in all_intersections:
    if len(inter_set) > max_length:
        longest_set = inter_set
        max_length = len(inter_set)

print(f"Longest intersection is [{', '.join([str(x) for x in longest_set])}] with length {len(longest_set)}")

