

number_of_lines = int(input())
cars = set([])

for turn in range(number_of_lines):
    line = input().split(", "
                            )
    command = line[0]
    plate = line[1]

    if command == "IN":
        cars.add(plate)
    elif command == "OUT":
        if plate in cars:
            cars.remove(plate)


if len(cars) == 0:
    print(f"Parking Lot is Empty")
else:
    print("\n".join(cars))




