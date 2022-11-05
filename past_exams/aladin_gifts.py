from collections import deque
from math import ceil

materials = list(map(int, input().split(" ")))
magic = deque(list(map(int, input().split(" "))))

items_crafted_dict = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}


def check_for_item(current_sum, item_dict):
    if 100 <= current_sum <= 199:
        item_dict["Gemstone"] += 1

    elif 200 <= current_sum <= 299:
        item_dict["Porcelain Sculpture"] += 1

    elif 300 <= current_sum <= 399:
        item_dict["Gold"] += 1

    elif 400 <= current_sum <= 499:
        item_dict["Diamond Jewellery"] += 1


while magic and materials:
    current_material = materials[-1]
    current_magic = magic[0]

    curr_sum = current_magic + current_material
    # print(curr_sum)

    if curr_sum < 100:
        if curr_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            curr_sum = current_magic + current_material
            check_for_item(curr_sum, items_crafted_dict)
            if curr_sum >= 100:
                materials.pop()
                magic.popleft()

            elif curr_sum < 100:
                materials.pop()
                magic.popleft()

        elif curr_sum % 2 != 0:
            curr_sum *= 2
            check_for_item(curr_sum, items_crafted_dict)
            if curr_sum >= 100:
                materials.pop()
                magic.popleft()
            elif curr_sum < 100:
                materials.pop()
                magic.popleft()

    elif 100 <= curr_sum <= 499:
        check_for_item(curr_sum, items_crafted_dict)
        materials.pop()
        magic.popleft()

    elif 499 < curr_sum:
        curr_sum = curr_sum/2
        curr_sum = ceil(curr_sum)
        check_for_item(curr_sum, items_crafted_dict)
        if curr_sum <= 499:
            materials.pop()
            magic.popleft()

        elif curr_sum > 499:
            materials.pop()
            magic.popleft()

    if len(materials) <= 0 or len(magic)<= 0:
        break

# print(items_crafted_dict)

presents_are_made = False

if items_crafted_dict["Gemstone"] > 0 and items_crafted_dict["Porcelain Sculpture"] > 0:
    presents_are_made = True
if items_crafted_dict["Gold"] > 0 and items_crafted_dict["Diamond Jewellery"] > 0:
    presents_are_made = True

if presents_are_made:
    print("The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if len(materials) > 0:
    print(f"Materials left: " + ', '.join(str(x) for x in materials))

if len(magic) > 0:
    print(f"Materials left: " + ', '.join(str(x) for x in magic))

final_dict = {}

for key,value in sorted(items_crafted_dict.items(), key=lambda kvpt: kvpt[0]):
    final_dict[key] = value

for ky, vl in final_dict.items():
    if vl >= 1:
        print(f"{ky}: {vl}")

#END