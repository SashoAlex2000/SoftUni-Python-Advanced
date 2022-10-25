first_set = set(int(x) for x in input().split(" "))
second_set = set(int(x) for x in input().split(" "))


number_of_lines = int(input())

for turn in range(number_of_lines):
    line = input().split()
    command = line[0]

    if command == "Add":
        if line[1] == "First":
            for i in range(2, len(line)):
                number = int(line[i])
                first_set.add(number)

        elif line[1] == "Second":
            for i in range(2, len(line)):
                number = int(line[i])
                second_set.add(number)

    elif command == "Remove":
        if line[1] == "First":
            for i in range(2, len(line)):
                number = int(line[i])
                if number in first_set:
                    first_set.remove(number)

        elif line[1] == "Second":
            for i in range(2, len(line)):
                number = int(line[i])
                if number in second_set:
                    second_set.remove(number)

    elif command == "Check":
        if first_set < second_set or second_set < first_set:
            print('True')
        else:
            print("False")

print(f", ".join(str(y) for y in sorted(first_set)))
print(f", ".join(str(y) for y in sorted(second_set)))
