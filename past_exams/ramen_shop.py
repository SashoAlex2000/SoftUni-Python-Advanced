

from collections import deque

bows_of_ramen = list(map(int, input().split(", ")))
customers = deque(list(map(int, input().split(", "))))

customers_served = False
ramen_is_over = False

while True:

    current_ramen = bows_of_ramen[-1]
    current_customer = customers[0]

    if current_ramen == current_customer:
        customers.popleft()
        bows_of_ramen.pop()

    elif current_ramen > current_customer:
        bows_of_ramen[-1] -= current_customer
        customers.popleft()

    elif current_customer > current_ramen:
        customers[0] -= current_ramen
        bows_of_ramen.pop()

    if len(bows_of_ramen) <= 0:
        ramen_is_over = True

    if len(customers) <= 0:
        customers_served = True

    if customers_served or ramen_is_over:
        break

if customers_served:
    print(f"Great job! You served all the customers.")
    if len(bows_of_ramen) > 0:
        print(f"Bowls of ramen left: " + ", ".join(str(x) for x in bows_of_ramen))

elif ramen_is_over:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: " + ", ".join(str(x) for x in customers))
