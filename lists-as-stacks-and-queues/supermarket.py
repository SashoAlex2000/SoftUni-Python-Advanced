from collections import deque
supermarket = deque()

line = input()

while line != "End":

    if line != "Paid":
        supermarket.append(line)

    elif line == "Paid":
        for i in range(len(supermarket)):
            print(supermarket.popleft())

    line = input()

print(f"{len(supermarket)} people remaining.")