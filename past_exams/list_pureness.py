#START
import sys
from sys import maxsize

def best_list_pureness(*args):
    # number_list = list(args)

    number_list = args[0]
    iterations = args[1]
    if len(number_list) == 0:
        return "Best pureness 0 after 0 rotations"

    if iterations == 0:
        current_sum = 0
        for element in number_list:
            current_sum += (element * number_list.index(element))

        return f"Best pureness {current_sum} after 0 rotations"

    if iterations == 0:
        current_sum = 0
        for element in number_list:
            current_sum += (element * number_list.index(element))

        return f"Best pureness {current_sum} after 0 rotations"

    best_rotation = 0
    current_rotation = 0
    max_sum = -sys.maxsize

    for turns in range(0, iterations):
        current_sum = 0
        for element in number_list:
            current_sum += (element * number_list.index(element))

        if current_sum > max_sum:
            max_sum = current_sum
            best_rotation = current_rotation

        # number_list.append(number_list.pop(0))
        number_list.insert(0,number_list.pop())
        current_rotation += 1

    return f"Best pureness {max_sum} after {best_rotation} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
