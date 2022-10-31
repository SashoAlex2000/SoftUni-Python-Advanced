
def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key = lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for name, quantities in sorted_cheese:
        result += name + "\n"
        result += "\n".join(str(x) for x in sorted(quantities, reverse=True)) + "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
