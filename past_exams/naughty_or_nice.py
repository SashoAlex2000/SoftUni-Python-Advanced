def naughty_or_nice_list(initial_list, *args, **kwargs):
    nice_list = []
    naughty = []
    not_found = []

    # print(args)
    # print(kwargs)

    for pair in initial_list:
        curr_num = int(pair[0])
        is_out = True
        for line in args:
            line_list = line.split("-")
            number = int(line_list[0])
            if curr_num == number:
                is_out = False

        if is_out:
            not_found.append(pair[1])


    for line in args:
        line_list = line.split("-")
        number = int(line_list[0])
        category = line_list[1]
        is_unique = True
        counter = 0
        current_name = ""

        for checks in initial_list:
            if checks[0] == number:
                current_name = checks[1]
                counter += 1
        if counter > 1:
            is_unique = False

        if is_unique:
            if category == "Naughty":
                naughty.append(current_name)
            elif category == "Nice":
                nice_list.append(current_name)
            else:
                not_found.append(current_name)

    for key, value in kwargs.items():

        if value == "Nice":
            if key not in nice_list and key not in naughty:
                nice_list.append(key)
            # if key in naughty:
            #     naughty.remove(key)

        if value == "Naughty":
            if key not in naughty and key not in nice_list:
                naughty.append(key)
            # if key in nice_list:
            #     nice_list.remove(key)

    for pair in initial_list:
        if pair[1] not in nice_list and pair[1] not in naughty and pair[1] not in not_found:
            not_found.append(pair[1])

    # result = " ".join(nice_list) + "!!!" + ' '.join(naughty) + "!!!" + ' '.join(not_found)

    for el in naughty:
        if el == "":
            naughty.remove(el)
    for el in nice_list:
        if el == "":
            nice_list.remove(el)

    for el in not_found:
        if el == "":
            not_found.remove(el)

    result = ""
    if len(nice_list) > 0:
        result += f"Nice: " + ", ".join(x for x in nice_list if x != "") + "\n"
    if len(naughty) > 0:
        result += f"Naughty: " + ", ".join(x.strip() for x in naughty if x.strip()) + "\n"
        # result += f"Naughty: " + ", ".join(list(filter(None, naughty))) + "\n"
    if len(not_found) > 0:
        result += f"Not found: " + ", ".join(x for x in not_found if x != "") + "\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
