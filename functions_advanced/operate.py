

from functools import reduce

a = [1,1,2,3,5,8]

print(reduce(lambda x,y: x+y, a))

def operate(sign, *args):
    if sign in ("+","-"):
        result = 0
    elif sign in ("*","/"):
        result = 1

    if sign == "+":
        for el in args :
            result += el
    if sign == "-":
        for el in args :
            result -= el
    if sign == "*":
        for el in args :
            result *= el
    if sign == "/":
        for el in args :
            result /= el
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))