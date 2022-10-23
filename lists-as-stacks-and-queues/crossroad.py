

green_time = int(input())
exit_time = int(input())

command = input()
traffic = []

while command != "END":
    traffic.append(command)
    command = input()

accident = False
passed_cars = 0

# while True:
#     timer = green_time
timer = green_time
hit_car_index = -1

for car in traffic:
    if car != "green" and timer > 0:
        timer -= len(car)
        passed_cars += 1
        if timer < 0:
            if abs(timer) > exit_time:
                accident = True
                hit_car_index = traffic.index(car)
                hit_letter = (len(car) - abs(timer)) + exit_time
    if car == "green":
        timer = green_time
    if accident:
        break

if accident:
    # print("crash")
    # # print(hit_car_index)
    hit_car = traffic[hit_car_index]
    # print(hit_car)
    # print(hit_car[hit_letter])
    print(f"A crash happened!")
    print(f"{hit_car} was hit at {hit_car[hit_letter]}.")
else:
    print(f"Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")



