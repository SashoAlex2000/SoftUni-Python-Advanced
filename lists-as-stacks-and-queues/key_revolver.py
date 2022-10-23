

bullet_price = int(input())
barrel_size = int(input())
bullet_list = list(map(int,input().split(" ")))
key_list = list(map(int,input().split(" ")))
itelligence_value = int(input())

# print(bullet_list)
# print(key_list)
used_bullets = 0
out_of_bullets = False
locks_unlocked = False
total_used_bullets = 0

while True:
    current_bullet = bullet_list[-1]
    current_hole = key_list[0]
    used_bullets += 1
    total_used_bullets += 1

    if current_bullet > current_hole:
        print("Ping!")
    else:
        print("Bang!")
        key_list.pop(0)
    bullet_list.pop(-1)



    if len(bullet_list) <= 0:
        out_of_bullets = True
    if len(key_list) <= 0:
        locks_unlocked = True

    if out_of_bullets:
        break
    if used_bullets >= barrel_size:
        print("Reloading!")
        used_bullets = 0
    if locks_unlocked:
        break


if locks_unlocked:
    print(f"{len(bullet_list)} bullets left. Earned ${itelligence_value - (total_used_bullets*bullet_price)}" )
elif out_of_bullets:
    print(f"Couldn't get through. Locks left: {len(key_list)}")
