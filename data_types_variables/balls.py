#xd
import sys
n = int(input())
current_best = -sys.maxsize
best_weight = 0
best_time = 0
best_quality = 0


for _ in range(n):
    weigth = int(input())
    time = int(input())
    quality = int(input())
    current_throw = (weigth / time) ** quality
    if current_throw > current_best:
        current_best = current_throw
        best_weight = weigth
        best_time = time
        best_quality = quality

print(f"{best_weight} : {best_time} = {int(current_best)} ({best_quality})")
