lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
armour_is_broken = False
armor = 0
helmet = 0
sword= 0
shield = 0

for i in range(1, lost_fights+1):
    if i % 2 == 0:
        helmet += 1
    if i % 3 == 0:
        sword += 1
    if i % 2 ==0 and i % 3 == 0:
        shield += 1
    if i % 2 ==0 and i % 3 == 0 and shield % 2 == 0:
        armour_is_broken = True
    if armour_is_broken:
        armor += 1
    armour_is_broken = False

total_expense = sword * sword_price + helmet_price * helmet + shield_price * shield + armour_price * armor
print(f"Gladiator expenses: {total_expense:.2f} aureus")