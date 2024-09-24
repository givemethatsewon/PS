from typing import *
from itertools import combinations

def is_prime(n: int) -> bool:
    # 3개의 서로다른 숫자를 더하므로 6 이상
    if n % 2 == 0:
        return False
    for k in range(3, int(n**(0.5)) + 1, 2):
        if n % k == 0:
            return False
    return True


def solution(nums: List[int]) -> int:
    cnt = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            cnt += 1
    return cnt