
n,m = [int(x) for x in input().split(" ")]
# print(type(n))
# print(type(m))
# print(m)

m_set = set()
n_set = set()

for turn in range(n):
    current_number = input()
    n_set.add(current_number)

for turn in range(m):
    current_number = input()
    m_set.add(current_number)


print(f"\n".join(n_set&m_set))