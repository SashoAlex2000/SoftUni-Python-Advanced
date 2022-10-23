from collections import deque

numbers = input().split(" ")
iterations = len(numbers)
numbers = deque(numbers)

for turn in range(iterations):
    print(numbers.pop(),end=" ")