

def list_manipulator(numbers, first_command,second_command, *args):

    if first_command == "add":
        if second_command == "beginning":
            if len(args) == 0:
                pass
            else:
                for element in reversed(args):
                    numbers.insert(0, element)

        elif second_command == "end":
            if len(args) == 0:
                pass
            else:
                for element in args:
                    numbers.append(element)

    elif first_command == "remove":
        if second_command == "beginning":
            if len(args) == 0:
                numbers.pop(0)
            else:
                iterations = int(args[0])
                for _ in range(iterations):
                    numbers.pop(0)


        elif second_command == "end":
            if len(args) == 0:
                numbers.pop()
            else:
                iterations = int(args[0])
                for _ in range(iterations):
                    numbers.pop()

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

