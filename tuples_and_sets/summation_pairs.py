# def getPairsCount(arr, n, sum):
#     count = 0  # Initialize result
#
#     # Consider all possible pairs
#     # and check their sums
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == sum:
#                 count += 1
#
#     return count

numbers = list(map(int, input().split()))
magic_sum = int(input())
# print(numbers)
# k = len(numbers) - 1
# i = 0
total_pairs = 0
total_iterations = 0
n = len(numbers)
pairs_set = set()


for i in range(n):
    for j in range(i+1,n):
        total_iterations += 1
        if numbers[i] + numbers[j] == magic_sum:
            print(f"{numbers[i]} + {numbers[j]} = {magic_sum}")
            total_pairs += 1
            current_tuple = (numbers[i], numbers[j])
            pairs_set.add(current_tuple)
print(f"Iterations done: {total_iterations}")
# print(total_pairs)

for pair in pairs_set:
    print(pair, end = "\n")
