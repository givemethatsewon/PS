import math
from itertools import permutations

def is_prime(n: int) -> bool:
    if n <= 1: 
        return False
    elif n == 2:
        return True
    elif n % 2 == 0: 
        return False
    for i in range(3, int(n**(0.5)) + 1, 2):
        if n % i == 0: 
            return False
    return True

def solution(numbers: str) -> int:
    digits = list(numbers)
    possible_numbers = set()
    for i in range(1, len(digits) + 1):
        # 순열 이용
        perms = permutations(digits, i)
        for p in perms: # p: tuple
            num = int(''.join(p))
            possible_numbers.add(num)
            
    primes = set()
    for num in possible_numbers:
        # 소수 검사
        if is_prime(num):
            primes.add(num)
    
    return len(primes)