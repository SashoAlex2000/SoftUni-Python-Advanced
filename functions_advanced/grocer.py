

def grocery_store(**kwargs):
    grocery_dict = {}

    for key, value in kwargs.items():
        if key not in grocery_dict.keys():
            grocery_dict[key] = value
    final_dict = {}
    for key,value in sorted(grocery_dict.items(), key = lambda kvpt: (-kvpt[1], -len(kvpt[0]), kvpt[0])):
        final_dict[key] = value
    result = ""

    for key, value in final_dict.items():
        result += f"{key}: {value}" + "\n"

    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


