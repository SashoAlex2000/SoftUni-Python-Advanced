from collections import deque
from math import floor


number_string = input().split()
# print(number_string)
special_symbols = ["*", "/", "+", "-"]
current_numbers = deque([])
current_result = 0
total_iterations = 0

for number in number_string:

    if number not in special_symbols:
        current_numbers.append(int(number))

    elif number in special_symbols and len(current_numbers) > 0:

        if number == "+":
            for k in range(len(current_numbers)):
                current_result += current_numbers[k]
            current_numbers.clear()
            total_iterations += 1

        elif number == "*":

            if total_iterations == 0:
                first_multi_sum = current_numbers[0]
                for k in range(1, len(current_numbers)):
                    first_multi_sum *= current_numbers[k]
                current_result = first_multi_sum
                total_iterations += 1
                current_numbers.clear()

            else:
                for k in range(len(current_numbers)):
                    current_result *= current_numbers[k]
                current_numbers.clear()
                total_iterations += 1
        elif number == "-":

            if total_iterations >= 1:
                for k in range(len(current_numbers)):
                    current_result -= current_numbers[k]
                current_numbers.clear()
                total_iterations += 1
            else:
                current_result = current_numbers[0]
                for k in range(1, len(current_numbers)):
                    current_result -= current_numbers[k]
                current_numbers.clear()
                total_iterations += 1

        elif number == "/":

            if total_iterations >= 1:
                # divisor = current_numbers[0]
                # for div in range(1, len(current_numbers)):
                #     divisor *= current_numbers[div]
                # current_result = floor(current_result / divisor)

                for k in range(0, len(current_numbers)):
                    current_result = floor(current_result / current_numbers[k])
                current_numbers.clear()
                total_iterations += 1
                # print("kur") # ?!?!?!

            else:
                current_result = current_numbers[0]
                for k in range(1, len(current_numbers)):
                    current_result = floor(current_result / current_numbers[k])
                current_numbers.clear()
                total_iterations += 1


print(current_result)


