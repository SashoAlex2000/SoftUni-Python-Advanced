
def is_valid(indx, lst):
    if 0 <= indx <len(lst):
        return True

    return False



def math_operations(*args, **kwargs):

    for quad in range(0, len(args), 4):
        if is_valid(quad, args):
            first_num = args[quad]
            # print(first_num)
            kwargs["a"] += first_num

        if is_valid(quad+1, args):
            second_num = args[quad+1]
            # print(second_num)

            kwargs["s"] -= second_num

        if is_valid(quad+2, args):

            third_num = args[quad+2]
            # print(third_num)

            if third_num != 0:
                kwargs["d"] /= third_num

        if is_valid(quad+3, args):
            fourth_num = args[quad+3]
            # print(fourth_num)

            kwargs["m"] *= fourth_num

    final_dict = {}
    for key, value in sorted(kwargs.items(), key =lambda kvpt: (-kvpt[1], kvpt[0])):
        final_dict[key] = value

    result = ""

    for ky, vl in final_dict.items():
        result += f"{ky}: {vl:.1f}\n"

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))