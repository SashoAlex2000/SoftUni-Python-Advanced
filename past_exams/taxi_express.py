from collections import deque


customers = deque(list(map(int, input().split(", "))))
taxi_divers = list(map(int, input().split(", ")))
total_time = 0
customers_left = False

while True:
    current_customer = customers[0]
    current_taxi = taxi_divers[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxi_divers.pop()

    else:
        taxi_divers.pop()

    if len(customers) == 0:
        break
    if len(taxi_divers) == 0:
        customers_left = True
        break

if customers_left:
    print("Not all customers were driven to their destinations")
    print("Customers left: " + ", ".join([str(x) for x in customers]))

else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
