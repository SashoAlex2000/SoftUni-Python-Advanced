

def numbers_searching(*args):
    unique_list = []
    duplicates = []
    missing_number = -10000

    for number in sorted(args):
        if number + 1 not in args and number != max(args):
            missing_number = number + 1
        if number not in unique_list:
            unique_list.append(number)
        else:
            duplicates.append(number)
    duplicates = sorted(list(set(duplicates)))

    return [missing_number,duplicates]



print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))