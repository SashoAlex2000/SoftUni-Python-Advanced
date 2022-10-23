clothes = list(map(int, input().split(" ")))

capacity = int(input())
current_stack = 0
total_baskets = 1

while True:
    current_cloth = clothes[0]
    new_capacity = current_cloth + current_stack

    if new_capacity < capacity:
        current_stack += current_cloth
        clothes.pop(0)

    elif new_capacity == capacity:
        total_baskets += 1
        clothes.pop(0)
        current_stack = 0

    elif new_capacity > capacity:
        total_baskets += 1
        clothes.pop(0)
        current_stack = current_cloth

    if len(clothes) <= 0:
        break
#

# while clothes:
#     current_basket = 0
#     total_baskets += 1
#     while True:
#         current_cloth = clothes[0]
#         current_basket += current_cloth
#         clothes.pop(0)
#
#         if current_basket < capacity:
#             continue
#         elif current_basket == capacity:
#             break
#         elif current_basket > capacity:
#             current_basket = current_cloth
#             break

print(total_baskets)