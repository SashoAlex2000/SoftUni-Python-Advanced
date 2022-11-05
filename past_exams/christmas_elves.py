def make_a_present(elf, mat):
    pass


from collections import deque

elves = deque(list(map(int, input().split(" "))))
materials = list(map(int, input().split(" ")))
total_energy = 0
total_iterations = 1
toys_made = 0

while True:
    current_elf = elves[0]

    while current_elf < 5:
        elves.popleft()
        if len(materials) <= 0 or len(elves) <= 0:
            break
        current_elf = elves[0]

    if len(materials) <= 0 or len(elves) <= 0:
        break

    current_materials = materials[-1]
    double_present = False
    fifth_present = False

    if total_iterations % 5 == 0:
        fifth_present = True

    if total_iterations % 3 == 0:
        current_materials *= 2
        double_present = True

    if not fifth_present:
        if current_elf >= current_materials:
            toys_made += 1
            current_elf -= current_materials
            current_elf += 1
            total_energy += current_materials
            materials.pop()
            elves[0] = current_elf
            elves.append(elves.popleft())
            if double_present:
                toys_made += 1

        else:
            current_elf *= 2
            elves[0] = current_elf
            elves.append(elves.popleft())

    if fifth_present:
        if current_elf < current_materials:
            current_elf *= 2
            elves[0] = current_elf
            elves.append(elves.popleft())
        else:
            total_energy += current_materials
            current_elf -= current_materials
            materials.pop()
            elves[0] = current_elf
            elves.append(elves.popleft())

    # print(elves)
    # print(materials)

    total_iterations += 1
    if len(materials) <= 0 or len(elves) <= 0:
        break


print(f"Toys: {toys_made}")
print(f"Energy: {total_energy}")

if len(elves) >0:
    print(f"Elves left: " + ", ".join(str(x) for x in elves))
if len(materials) >0:
    print(f"Boxes left: " + ", ".join(str(x) for x in materials))

