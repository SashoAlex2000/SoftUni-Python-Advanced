
number_of_lines = int(input())
element_set = set()

for turn in range(number_of_lines):
    current_list = input().split(" ")
    for el in current_list:
        element_set.add(el)


print(f"\n".join(element_set))
