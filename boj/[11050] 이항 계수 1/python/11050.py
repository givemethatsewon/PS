from itertools import combinations

n, k = map(int, input().split())

# combination 수행할 리스트
combis = list(combinations(range(n), k))

print(len(combis))