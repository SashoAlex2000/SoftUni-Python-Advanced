def check_if_magic(current_index, list_of_pumps):
    start_point = 0
    beginning_gas = list_of_pumps[0]
    first_distance = list_of_pumps[1]
    gas_in_tank = 0

    if beginning_gas < first_distance:
        return False

    else:
        gas_in_tank = 0 + beginning_gas - first_distance
        range_to_check = int((len(list_of_pumps) + 1) / 2)
        # for check in range(len(list_of_pumps) + 1):
        checking_index = 0

        for check in range(range_to_check):
            if checking_index == 0:
                pass
            else:
                curr_gas = list_of_pumps[checking_index]
                curr_distance = list_of_pumps[checking_index + 1]
                gas_in_tank += curr_gas

                if curr_distance <= gas_in_tank:
                    gas_in_tank -= curr_distance

                else:
                    return False

            checking_index += 2
    return current_index


number_of_pumps = int(input())
pump_list = []

for _ in range(number_of_pumps):
    line = list(map(int, input().split()))
    amount_of_petrol = line[0]
    distance = line[1]
    pump_list.append(amount_of_petrol)
    pump_list.append(distance)

thing_to_print = -1
# print(pump_list)
# print(pump_list)
# print(check_if_magic(0, pump_list))
range_of_pumps = int((len(pump_list) + 1) / 2)
place_to_start = 0
for _ in range(range_of_pumps):
    # print(check_if_magic(palce_to_start, pump_list))
    if check_if_magic(place_to_start, pump_list):
        thing_to_print = check_if_magic(place_to_start, pump_list)
        break

    pump_list.pop(0)
    pump_list.pop(0)
    place_to_start += 1

print(thing_to_print)
