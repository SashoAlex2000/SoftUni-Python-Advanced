#DONE FROM THE LAPTOP

#START
from collections import deque

males = list(map(int,input().split(" ")))
females = deque(list(map(int,input().split(" "))))

males_over = False
females_over = False
matches = 0

while True:
    if len(males) == 0:
        males_over = True
        break
    if len(females) == 0:
        females_over = True
        break


    current_male = males[-1]
    current_female = females[0]

    # print(f"{current_male} {current_female}")
    # print(males)

    if current_male <= 0 and len(males) == 1:
        males_over = True
        break

    if (current_female <= 0 and len(females) == 1) or len(females) == 0:
        females_over = True
        break


    if current_male <=0:
        # while current_male <=0:
        males.pop()
        current_male = males[-1]
        continue

    if current_female <= 0:
        # while current_female <= 0:
        females.popleft()
        current_female = females[0]
        continue

    if current_male % 25 == 0 or current_female % 25 == 0:
        if current_male % 25 == 0:
            males.pop()
            males.pop()
            continue

        elif current_female % 25 == 0:
            females.popleft()
            females.popleft()
            continue

    if current_male == current_female:
        males.pop()
        females.popleft()
        matches += 1
    else:
        current_male -=2
        females.popleft()
        males.pop()
        males.append(current_male)

    if len(males) <= 0:
        males_over = True
    if len(females) <= 0:
        females_over = True

    if females_over or males_over:
        break

# print(females)
for male in males:
    if male <= 0:
        males.remove(male)

if len(males) <= 0:
    males_over = True


females = list(females)

for female in females:
    if female <= 0:
        females.remove(female)


if len(females) <= 0:
    females_over = True

print(f"Matches: {matches}")

if males_over:
    print("Males left: none"
          )
else:
    print(f"Males left: " + f", ".join(str(x) for x in reversed(males)))


if females_over:
    print("Females left: none")
else:
    reverse_females = reversed(list(females))
    print(f"Females left: " + f", ".join(str(x) for x in reversed(list(reverse_females))))

#END
