
number_of_lines = int(input())
username_set = set()

for turn in range(number_of_lines):
    username = input()
    username_set.add(username)

print(f"\n".join(username_set))
