

sublists = input().split("|")

result = []

for idx in range(len(sublists)-1,-1,-1):
    result.extend(sublists[idx].strip().split())

print(' '.join(result))
