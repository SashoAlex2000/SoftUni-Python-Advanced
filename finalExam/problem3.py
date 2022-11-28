#SHOPPING CART

def shopping_cart(*args):
    soup_limit = 3
    pizza_limit = 4
    dessert_limit = 2

    product_dict = {"Soup": [], "Pizza": [], "Dessert": []}
    iterations = 0
    for iter in args:
        if type(iter) == str:
            # print("END")
            if iterations == 0:
                return "No products in the cart!"
            for key, value in product_dict.items():
                new_value = sorted(value)
                product_dict[key] = new_value

            print_dict = dict(sorted(product_dict.items(), key = lambda kpvt: (-len(kpvt[1]), kpvt[0])))
            # for item in print_dict:
            #     print(type(item))
            result = ""
            for key, value in print_dict.items():
                result += f"{key}:\n"
                for item in value:
                    result += f" - {item}\n"


            return result

        iterations += 1
        product, ingredient = iter
        # print(product, ingredient)
        if product in product_dict.keys():
            if product == "Soup":
                if len(product_dict[product]) < soup_limit:
                    if ingredient not in product_dict[product]:
                        product_dict[product].append(ingredient)

            elif product == "Pizza":
                if len(product_dict[product]) < pizza_limit:
                    if ingredient not in product_dict[product]:
                        product_dict[product].append(ingredient)

            elif product == "Dessert":
                if len(product_dict[product]) < dessert_limit:
                    if ingredient not in product_dict[product]:
                        product_dict[product].append(ingredient)

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
