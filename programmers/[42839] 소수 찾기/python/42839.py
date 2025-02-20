from typing import *
import math
from itertools import permutations

def solution(numbers: str) -> int:
    cnt = 0
    number_list: List[str] = [s for s in numbers]
    nums = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(number_list, i)
        nums.update(int(''.join(perm)) for perm in perms)
        print(nums)
    for num in nums:
        if isPrime(num):
            cnt += 1
    
    return cnt

def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # 홀수만 처리
        end = int(math.sqrt(num))
        for i in range(3, end + 1, 2):
            if num % i == 0:
                return False
    return True

                
        