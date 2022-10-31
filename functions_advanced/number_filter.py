

def even_odd_filter(**kwargs):
    my_dict = {"even":[], "odd": []}

    for kvpt in kwargs.items():
        key_word = kvpt[0]
        # print(kvpt[0])
        # print(kvpt[1])

        if key_word == "even":
            for num in kvpt[1]:
                if num % 2 == 0:
                    my_dict["even"].append(num)
        elif key_word == "odd":
            for num in kvpt[1]:
                if num % 2 != 0:
                    my_dict["odd"].append(num)

    result_dict = dict()
    for key, value in sorted(my_dict.items(), key= lambda kvp: kvp[1], reverse= True):
        if len(value) > 0:
            result_dict[key] = value

    # return sorted(my_dict.items(), key= lambda kvp: kvp[1], reverse= True)
    return result_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
