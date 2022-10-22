from collections import deque

dispenser_liters = int(input())
names = deque()
name = input()

while name != "Start":
    names.append(name)
    name = input()

line = input()

while line != "End":
    command = line.split(" ")
    if len(command) == 1:
        current_liters = int(command[0])
        if dispenser_liters >= current_liters:
            dispenser_liters -= current_liters
            print(f"{names.popleft()} got water")
        else:
            print(f"{names.popleft()} must wait" )

    elif len(command) > 1:
        liters_to_add = int(command[1])
        dispenser_liters += liters_to_add

    line = input()

print(f"{dispenser_liters} liters left")