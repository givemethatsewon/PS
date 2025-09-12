from math import sqrt

# m, n 입력 받기
m, n = map(int, input().split())

# 배열 초기화
primes = [True] * (n + 1)
primes[0] = primes[1] = False # 0과 1은 소수가 아님!

for i in range(2, int(sqrt(n)) + 1):
    if primes[i]:
        for j in range(i*i, n + 1, i):
            primes[j] = False

prime_nums = [i for i, is_prime in enumerate(primes) if is_prime and i >= m]

print(*prime_nums, sep='\n')