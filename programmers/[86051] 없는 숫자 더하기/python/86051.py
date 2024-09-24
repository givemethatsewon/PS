from typing import *

def solution(numbers: List[int])->int:
    ans = 0
    for i in range(10):
        if i not in numbers:
            ans += i
    return ans