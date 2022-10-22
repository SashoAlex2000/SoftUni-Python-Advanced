text = input()
parentesis = []

for i in range(len(text)):
    if text[i] == "(":
        parentesis.append(i)
    elif text[i] == ")":
        start_index = parentesis.pop()
        print(text[start_index:i+1])

