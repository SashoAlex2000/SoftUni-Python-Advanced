from collections import deque

total_quantity = int(input())
orders = list(map(int, input().split(" ")))
biggest_order = max(orders)


while orders:
    current_order = orders[0]
    if total_quantity >= current_order:
        total_quantity -= current_order
        orders.pop(0)
    else:
        break

orders = [str(i) for i in orders]

print(biggest_order)
if orders:
    print("Orders left:", end=" ")
    print(" ".join(orders))
else:
    print("Orders complete")
