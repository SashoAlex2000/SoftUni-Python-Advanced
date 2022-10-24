from math import floor
number_of_lines = int(input())

odd_set = set()
even_set = set()
current_row = 1

for turn in range(number_of_lines):
    current_name = list(input())
    current_sum = 0

    for char in current_name:
        current_sum += ord(char)

    current_sum = floor(current_sum / current_row)

    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

    current_row += 1

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)

set_to_print = ""

if odd_set_sum == even_set_sum:
    set_to_print = odd_set_sum | even_set_sum
elif odd_set_sum > even_set_sum:
    set_to_print = odd_set - even_set
elif odd_set_sum < even_set_sum:
    set_to_print = odd_set ^ even_set

print(f", ".join([str(x) for x in set_to_print]))




