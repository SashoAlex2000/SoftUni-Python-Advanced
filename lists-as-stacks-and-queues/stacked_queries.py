stack = []
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "1":
        number = int(line[1])
        stack.append(number)
    elif command == "2" and stack:
        stack.pop()
    if command == "3" and stack:
        print(max(stack))
    if command == "4" and stack:
        print(min(stack))

while stack:
    element = stack.pop()
    if stack:
        print(element, end= ", ")
    else:
        print(element)