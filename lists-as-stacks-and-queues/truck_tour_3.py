from collections import deque


def check_circle(pump_list):
    magic_point = pump_list[0][0]

    start_gas = pump_list[0][1]
    start_distance = pump_list[0][2]

    total_gas = 0
    if start_gas < start_distance:
        # print("first False")
        return False
    else:
        total_gas += start_gas
        total_gas -= start_distance

        for turn in range(1, len(pump_list)):
            current_gas = pump_list[turn][1]
            current_distance = pump_list[turn][2]
            total_gas += current_gas

            if total_gas < current_distance:
                return False
                # print("second False")
            else:
                total_gas -= current_distance

        return magic_point


number_of_pumps = int(input())
beginning_list = [[] for _ in range(number_of_pumps)]

for t in range(number_of_pumps):
    line = list(map(int, input().split()))
    amount_of_petrol = line[0]
    distance = line[1]

    beginning_list[t].append(t)
    beginning_list[t].append(amount_of_petrol)
    beginning_list[t].append(distance)

# print(beginning_list)
pump_deque = deque(beginning_list)
# print(pump_deque)


while True:
    if check_circle(pump_deque) == False:
        pump_deque.rotate(-1)
    else:
        break

print(check_circle(pump_deque))