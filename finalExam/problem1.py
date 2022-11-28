#COLLECTING EGGS

from collections import deque

eggs = deque(list(map(int, input().split(", "))))
paper_pieces = list(map(int, input().split(", ")))

boxes_filled = 0
eggs_over = False

while True:
    if eggs_over:
        break

    current_egg = eggs[0]
    current_paper = paper_pieces[-1]

    if current_egg <= 0:
        if len(eggs) > 1:
            eggs.popleft()
            continue
        elif len(eggs) == 1:
            eggs.popleft()
            eggs_over = True
            continue

    if current_egg == 13:
        new_first = paper_pieces[-1]
        new_last = paper_pieces[0]

        # print(new_first)
        # print(new_last)

        paper_pieces[0] = new_first
        paper_pieces[-1] = new_last

        # print("Bad luck")
        if len(eggs) > 1:
            eggs.popleft()
            continue
        elif len(eggs) == 1:
            eggs.popleft()
            eggs_over = True
            continue

        # paper_pieces[0], paper_pieces[-1] = paper_pieces[-1], paper_pieces[0]


    current_sum = current_egg + current_paper
    # print(current_sum)

    if current_sum <= 50:
        boxes_filled += 1

        eggs.popleft()
        paper_pieces.pop()

    else:
        eggs.popleft()
        paper_pieces.pop()

    if len(eggs) <= 0 or len(paper_pieces) <= 0 :
        break

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print("Eggs left: " + ", ".join(str(x) for x in eggs))

if paper_pieces:
    print("Pieces of paper left: " + ", ".join(str(x) for x in paper_pieces))