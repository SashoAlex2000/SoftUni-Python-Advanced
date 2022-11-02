from simple_operations.helper import operation_mapper


data = input().split()

a = float(data[0])
sign = data[1]
b = float(data[2])

# print(operation_mapper[sign](a,b))
try:
    result = operation_mapper[sign](a,b)
    print(f"{result:.2f}")
except ZeroDivisionError:
    print("Invalid second number - b shouldn't be 0")