

nums = (float(el) for el in input().split())

occurances = {}


for num in nums:
    if num not in occurances.keys():
        occurances[num] = 1
    else:
        occurances[num] += 1

# print(occurances)

for number, occ in occurances.items():  # <-- that's when we have used tuples, in unpacking
    print(f"{number} - {occ} times")

# for kvp in occurances.items():
#     print(kvp)
#     print(type(kvp))