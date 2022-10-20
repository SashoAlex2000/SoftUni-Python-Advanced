# (IASJDF)(UASDUNA(USDN))

year = int(input())
current_year = year
is_unique = False
empty_list = []

while True:
    current_division_year = current_year
    for i in range(len(str(current_year))):
        empty_list.append(current_division_year //(len - i)
        current_division_year = current_division_year - empty_list[i] *




    current_year += 1

    m = current_year // 1000

    n = (current_year - m * 1000) // 100
    l = (current_year - m * 1000 - n * 100) // 10
    k = current_year - m * 1000 - n * 100 - l * 10
    if  m != n and m != l and m != k and n != l and n != k and l != k:
        is_unique = True
    if is_unique:
        break

print(current_year)

