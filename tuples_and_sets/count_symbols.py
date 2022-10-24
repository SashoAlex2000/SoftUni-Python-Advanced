

char_list = list(input())
char_dict = {}

for char in char_list:

    if char not in char_dict:
        char_dict[char] = 0

    char_dict[char] += 1

# print(char_dict)
new_dict = sorted(char_dict.keys())

for kvp in new_dict:
    character = kvp
    occ = char_dict[character]
    print(f"{character}: {occ} time/s")
