def stock_availability(flavor_list, *args):
    command = args[0]

    if command == "delivery":
        if len(args) == 1:
            return flavor_list

        else:
            for item in range(1, len(args)):
                flavor_list.append(args[item])
            return flavor_list


    elif command == "sell":
        if len(args) == 1:
            flavor_list.pop(0)
            return flavor_list
        else:
            for item in range(1, len(args)):
                curr_item = args[item]
                if isinstance(curr_item, int):
                    for turn in range(curr_item):
                        flavor_list.pop(0)

                else:
                    if curr_item in flavor_list:
                        while curr_item in flavor_list:
                            flavor_list.remove(curr_item)

            return flavor_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

# END
