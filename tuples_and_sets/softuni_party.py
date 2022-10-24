

number_of_lines = int(input())
guests = set()
vip_guests = set()


for turn in range(number_of_lines):
    line = input()

    if line[0].isdigit():
        vip_guests.add(line)
    else:
        guests.add(line)

command = input()

while command != "END":
    if command[0].isdigit():
        vip_guests.remove(command)
    else:
        guests.remove(command)

    command = input()

total_missing = len(vip_guests) + len(guests)
print(f"{total_missing}")
print("\n".join(sorted(vip_guests)))
print("\n".join(sorted(guests)))
