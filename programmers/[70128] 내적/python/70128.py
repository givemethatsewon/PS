from itertools import product
from typing import *


def solution(a: List[int], b: List[int]) -> int:
    ans = 0
    for x, y in zip(a, b):
        ans += x * y
        
    return ans