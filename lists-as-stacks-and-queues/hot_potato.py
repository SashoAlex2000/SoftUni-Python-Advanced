from collections import deque
list_kids = input().split(" ")

kids = deque(list_kids)

turns = int(input())

while True:
    current_potato = len(kids)
    index_to_remove = 0
    passes = 0

    while passes < turns:
        current_potato += 1
    




