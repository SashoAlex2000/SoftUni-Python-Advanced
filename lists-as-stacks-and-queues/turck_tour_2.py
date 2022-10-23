
def check_distance(start_point, dict_of_pumps):
    start_gas = dict_of_pumps[start_point][0]
    start_distance = dict_of_pumps[start_point][1]
    total_petrol = 0

    if start_gas < start_distance:
        return False
    else:
        total_petrol += start_gas
        total_petrol -= start_distance
        for curr in range(start_point + 1, len(dict_of_pumps)):


            current_petrol = dict_of_pumps[curr][0]
            current_km = dict_of_pumps[curr][1]
            total_petrol += current_petrol
            if total_petrol < current_km:
                print(f"Failed at {curr}")
                return False
            else:
                print(f"Continuing at {curr})")
                total_petrol -= current_km

        return start_point


number_of_pumps = int(input())
pump_dict = {}

for i in range(number_of_pumps):
    line = list(map(int, input().split()))
    amount_of_petrol = line[0]
    distance = line[1]
    pump_dict[i] = []
    pump_dict[i].append(amount_of_petrol)
    pump_dict[i].append(distance)

thing_to_print = -1
total_gas = 0
# print(pump_dict)
for turn in range(len(pump_dict)):
    # print(turn)

    thing_to_print = check_distance(turn,pump_dict)
    if thing_to_print != False and thing_to_print != -1:
        break

print(thing_to_print)