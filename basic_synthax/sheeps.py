sheep = input()

sheep_list = list(sheep)
sheep_list.reverse()



# sheep_counter = 0
# if "sheep" in sheep:
#     print("cici")
# print(sheep_counter)
sheep_counter = 0
for element in sheep_list:
    if element == "p":
        sheep_counter += 1
    if element == "w":
        wolf_position = sheep_counter + 1
        sheep_counter += 1


if wolf_position == 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_position - 1}! You are about to be eaten by a wolf!" )