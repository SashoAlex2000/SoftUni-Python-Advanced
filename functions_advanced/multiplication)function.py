def multiply(*args, **kwargs):

    if kwargs:
        print("kwargs exists!!!")
    total_sum = args[0]
    for element in args[1:]:
        total_sum *= element
    return total_sum



print(multiply(1, 4, 5, name = "goshi"))
print(multiply(4, 5, 6, 1, 3,546,645,564,13,4,1))
print(multiply(2, 0, 1000, 5000))
