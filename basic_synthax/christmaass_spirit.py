quantity = int(input())
days = int(input())
total_budget = 0
total_spirit = 0

for i in range(1, days+1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_spirit += 5
        total_budget += quantity * 2
    if i % 3 == 0:
        total_spirit += 13
        total_budget += quantity * 5
        total_budget += quantity * 3
    if i % 5 == 0:
        total_spirit += 17
        total_budget += quantity * 15
        if i % 5 == 0 and i % 3 == 0:
            total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        total_budget += 23


if days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_budget}")
print(f"Total spirit: {total_spirit}")