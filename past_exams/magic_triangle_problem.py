
def get_magic_triangle(n):
    magic_list = []

    for row in range(1, n+ 1):
        # print(f"row:{row}")

        if row == 1:
            current_list = [1]
            magic_list.append(current_list)

        else:
            current_list = []

            for position in range(1,row+1):
                if position == 1 or position == row:
                    curr_number = 1
                    current_list.append(curr_number)
                else:
                    current_number = magic_list[row-2][position-2] + magic_list[row-2][position-1]
                    current_list.append(current_number)

            magic_list.append(current_list)

    return magic_list


print(get_magic_triangle(1))
print(get_magic_triangle(2))
print(get_magic_triangle(3))
print(get_magic_triangle(5))
print(get_magic_triangle(25))
