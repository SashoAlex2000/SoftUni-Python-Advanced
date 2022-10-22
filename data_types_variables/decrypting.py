key = int(input())
number_of_lines = int(input())
empty_list = []


for _ in range(number_of_lines):
    ch = input()
    thing_to_append = ord(ch) + key
    empty_list.append(chr(thing_to_append))

print("".join(empty_list))