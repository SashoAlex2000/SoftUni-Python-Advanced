from collections import deque

cups_list = list(map(int, input().split(" ")))
bottles_list = list(map(int, input().split(" ")))

cups_list = deque(cups_list)
# print(cups_list)
# print(bottles_list)

bottles_are_over = False
cups_are_filled = False
turns = len(bottles_list)
total_wasted_litters = 0

for turn in range(turns):
    current_bottle = bottles_list.pop()

    cups_list[0] -= current_bottle

    if cups_list[0] < 0:
        total_wasted_litters += abs(cups_list[0])
        cups_list.popleft()
    elif cups_list[0] == 0:
        cups_list.popleft()

    if len(cups_list) <= 0:
        cups_are_filled = True
    if len(bottles_list) <= 0:
        bottles_are_over = True

    if bottles_are_over or cups_are_filled:
        break

if cups_are_filled:
    print("Bottles: ",end ="")
    for bottle in bottles_list:
        print(bottle, end = " ")

elif bottles_are_over:
    print(f"Cups: ",end = "")
    for cup in cups_list:
        print(cup, end =" ")

print(f"\nWasted litters of water: {total_wasted_litters}")

