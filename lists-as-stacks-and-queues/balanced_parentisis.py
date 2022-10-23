

opening_symbols = ["(", "{", "["]
text = input()
print(text)

first_part = []
second_part = []

for symbol in text:
    if symbol in opening_symbols:
        first_part.append(symbol)
    else:
        second_part.append(symbol)

is_equal = True

# if len(first_part) != len(second_part):
#     is_equal = False

for turn in range(1, int(len(text) / 2) + 1):
    if text[turn - 1] == text[turn]:
        pass
    else:
        is_equal = False
        break


print(first_part)
print(second_part)
if is_equal:
    print('Yes')
else:
    print('No')
