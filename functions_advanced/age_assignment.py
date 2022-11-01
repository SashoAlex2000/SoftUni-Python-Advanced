
def age_assignment(*args, **kwargs):
    initial_name_dict = {}

    for name in args:
        initial_name_dict[name] = 0

    for key, value in kwargs.items():
        for name in initial_name_dict.keys():
            if key == name[0]:
                initial_name_dict[name] += value
                break
    final_dict = {}
    for name, age in sorted(initial_name_dict.items(), key = lambda kvpt: kvpt[0]):
        final_dict[name] = age

    result = ""

    for name, age in final_dict.items():
        result += f"{name} is {age} years old.\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
