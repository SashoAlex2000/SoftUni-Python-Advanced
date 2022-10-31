

def sorting_cheeses(**kwargs):
    value_list = []
    value_set = set()
    equal_pieces = False
    for key, value in kwargs.items():
        len_v = len(value)
        value_list.append(len_v)
        value_set.add(len_v)
    print(value_list)
    print(value_set)
    if len(value_set) != len(value_list):
        equal_pieces = True

    if equal_pieces:
        # sortedcheeses = sorted(kwargs.keys(), key=lambda x: x.lower())
        for key in sorted(kwargs.keys(), key=lambda x: x.lower()):
            print(key)
            print(*kwargs[key], sep="\n")
    else:
        for key, value in sorted(kwargs.items(), key=lambda x:sum(x[1]), reverse=True):
            print(key)
            print(*value, sep="\n")


sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125])

print("!"*10)

sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )

