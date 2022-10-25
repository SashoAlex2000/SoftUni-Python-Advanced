from collections import deque


chocolates = list(map(int,input().split(", ")))
milk = deque(list(map(int,input().split(", "))))

chocolates_over = False
milk_over = False
enough_milkshakes = False
milkshakes_made = 0

while True:
    if chocolates[-1] <= 0:
        if len(chocolates) == 1:
            chocolates.pop()
            chocolates_over = True
            break

        while chocolates[-1] <= 0:
            chocolates.pop()
    if milk[0] <= 0:
        if len(milk) == 1:
            milk.popleft()
            milk_over = True
            break

        while milk[0] <= 0:
            milk.popleft()

    current_chocolate = chocolates[-1]
    current_milk = milk[0]

    if current_chocolate == current_milk:
        milkshakes_made += 1
        milk.popleft()
        chocolates.pop()
        # print("Made a milkshake!")
    else:
        milk.append(milk.popleft())
        chocolates[-1] -= 5

    if milkshakes_made >= 5:
        enough_milkshakes = True

    if len(milk) <=0:
        milk_over = True

    if len(chocolates) <=0:
        chocolates_over = True

    if milk_over or chocolates_over or enough_milkshakes:
        break


if enough_milkshakes:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolates_over:
    print("Chocolate: empty")
else:
    print("Chocolate: " + ", ".join(str(x) for x in chocolates))

if milk_over:
    print("Milk: empty")
else:
    print("Milk: " + ", ".join(str(x) for x in milk))

