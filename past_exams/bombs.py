#START
from collections import  deque

effects = deque(list(map(int,input().split(", "))))
casings = list(map(int,input().split(", ")))

values = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
found_bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

effects_over = False
casings_over = False
bomb_pouch_filled = False

while True:
    current_effect = effects[0]
    current_casing = casings[-1]

    current_sum = current_casing + current_effect

    if current_sum in values.keys():
        bomb_found = values[current_sum]
        found_bombs[bomb_found] += 1
        casings.pop()
        effects.popleft()

    else:
        casings[-1] -= 5

    if len(effects) <= 0 :
        effects_over = True
    if len(casings) <= 0 :
        casings_over = True

    if found_bombs["Datura Bombs"] >=3 and found_bombs["Cherry Bombs"] >=3 and found_bombs["Smoke Decoy Bombs"] >=3:
        bomb_pouch_filled = True

    if effects_over or casings_over or bomb_pouch_filled:
        break


if bomb_pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects_over:
    print("Bomb Effects: empty")
else:
    print("Bomb Effects: " + ", ".join([str(x) for x in effects]))
if casings_over:
    print("Bomb Casings: empty")
else:
    print("Bomb Casings: " + ", ".join([str(x) for x in casings]))

for key, value in sorted(found_bombs.items()):
    print(f"{key}: {value}")

