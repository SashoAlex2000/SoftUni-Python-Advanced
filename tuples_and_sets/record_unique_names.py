

number_of_lines = int(input())
names = []

for turn in range(number_of_lines):
    name = input()
    names.append(name)

set_names = set(names)
print("\n".join(set_names))