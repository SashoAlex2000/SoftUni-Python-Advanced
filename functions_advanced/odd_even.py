
def odd_even_sum(com, lst):
    odd_sum = 0
    even_sum = 0
    length = len(lst)
    for num in lst:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    if com == "Odd":
        print(odd_sum * length)
    else:
        print(even_sum * length)


command = input()

num_list = [int(x) for x in input().split(" ")]

odd_even_sum(command,num_list)