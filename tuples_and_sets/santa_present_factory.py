from collections import deque

materials = list(map(int, input().split(" ")))
magic_integers = deque(list(map(int, input().split(" "))))

magic_goods = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

crafted_goods_dict = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while True:
    current_material = materials[-1]
    current_magic_integer = magic_integers[0]

    sum_current = current_material * current_magic_integer
    # print(sum_current)

    if sum_current == 0:
        if current_material == 0:
            materials.pop()
        if magic_integers[0] == 0:
            magic_integers.popleft()

    elif sum_current in magic_goods.keys():
        # print(f"sum{sum_current} is magic")
        present = magic_goods[sum_current]
        crafted_goods_dict[present] += 1
        materials.pop()
        magic_integers.popleft()

    elif sum_current < 0:
        thing_to_add = current_material + current_magic_integer
        materials.pop()
        magic_integers.popleft()
        materials.append(thing_to_add)

    elif sum_current > 0:
        magic_integers.popleft()
        materials[-1] += 15

    if len(materials) == 0 or len(magic_integers) == 0:
        break

# print(crafted_goods_dict)

magic_pairs = False

if crafted_goods_dict["Doll"] >= 1 and crafted_goods_dict["Wooden train"] >= 1:
    magic_pairs = True
if crafted_goods_dict["Teddy bear"] >= 1 and crafted_goods_dict["Bicycle"] >= 1:
    magic_pairs = True

if magic_pairs:
    print("The presents are crafted! Merry Christmas!")
else:print("No presents this Christmas!")

if materials:
    materials.reverse()
    print(f"Materials left: " + ', '.join(str(x) for x in materials))
if magic_integers:
    print(f"Magic  left: " + ', '.join(str(x) for x in magic_integers))

for kvp in sorted(crafted_goods_dict.items()):
    present_print = kvp[0]
    occ = kvp[1]

    if occ > 0:
        print(f"{present_print}: {occ}")