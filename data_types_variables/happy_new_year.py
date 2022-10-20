year = int(input())
is_happy = False
while True:
    my_list = []
    year += 1
    current_year = str(year)
    for ch in current_year:
        my_list.append((ch))

    my_set = set(my_list)
    if len(my_set) != len(my_list):
        pass
    else:
        is_happy = True

    if is_happy:
        break

    my_list = []

print(year)
#set(current_year)
