




def multiply_numbers(num1,num2):
    return num1*num2
def sum_numbers(num1,num2):
    return num1 + num2


def func_executor(*args):
    first_tuple = args[0]
    second_tuple = args[1]
    func_name_1 = first_tuple[0]
    func_name_2 = second_tuple[0]
    arguments_1 = first_tuple[1]
    arguments_2 = second_tuple[1]


    # print(first_tuple)
    # print(second_tuple)
    result = ""

    if func_name_1.__name__ == "multiply_numbers":
        result += f"{func_name_1.__name__} - {multiply_numbers(arguments_1[0], arguments_1[1])}" + "\n"
        # return multiply_numbers(arguments_1[0], arguments_1[1])

    elif func_name_1.__name__ == "sum_numbers":
        result += f"{func_name_1.__name__} - {sum_numbers(arguments_1[0], arguments_1[1])}" + "\n"

    if func_name_2.__name__ == "multiply_numbers":
        result += f"{func_name_2.__name__} - {multiply_numbers(arguments_2[0], arguments_2[1])}" + "\n"

    elif func_name_2.__name__ == "sum_numbers":
        result += f"{func_name_2.__name__} - {sum_numbers(arguments_2[0], arguments_2[1])}" + "\n"

    return result


# print(func_executor(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
# ))

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
