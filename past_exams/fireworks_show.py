
from collections import deque

created_fireworks_dict = {"Palm":0,"Willow":0,"Crossette":0}

firework_effect = deque(list(map(int, input().split(", "))))
explosive_power = list(map(int, input().split(", ")))
materials_over = False
fireworks_done = False

while True:

    current_firework = firework_effect[0]
    current_explosive = explosive_power[-1]
    curr_sum = current_explosive + current_firework

    if current_firework <=0:
        if len(firework_effect) > 1:
            firework_effect.popleft()
            continue
        else:
            firework_effect.popleft()
            break
    if current_explosive <=0:
        if len(explosive_power) > 1:
            explosive_power.pop()
            continue
        else:
            explosive_power.pop()
            break

    if curr_sum % 3 ==0 or curr_sum % 5 ==0:
        if curr_sum % 3 == 0 and curr_sum % 5 != 0:
            created_fireworks_dict["Palm"] +=1

        if curr_sum % 3 != 0 and curr_sum % 5 == 0:
            created_fireworks_dict["Willow"] += 1

        if curr_sum % 3 == 0 and curr_sum % 5 == 0:
            created_fireworks_dict["Crossette"] +=1

        firework_effect.popleft()
        explosive_power.pop()

    else:
        current_firework -= 1
        firework_effect.popleft()
        firework_effect.append(current_firework)

    if len(explosive_power) <= 0 or len(firework_effect) <= 0:
        materials_over = True

    if created_fireworks_dict["Palm"] >= 3 and created_fireworks_dict["Willow"] >= 3 and \
            created_fireworks_dict["Crossette"] >= 3:
        fireworks_done = True

    if materials_over or fireworks_done:
        break

# print(firework_effect)
# print(explosive_power)
# print(created_fireworks_dict)

if fireworks_done:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if len(firework_effect) > 0:
    print("Firework Effects left: " + ", ".join(str(x) for x in firework_effect))
if len(explosive_power) > 0:
    print("Explosive Power left: " + ", ".join(str(x) for x in explosive_power))

for key, value in created_fireworks_dict.items():
    print(f"{key} Fireworks: {value}")