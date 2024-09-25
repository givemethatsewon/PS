from typing import *
from itertools import combinations

def solution(numbers: List[int]) -> List[int]:
    combis = combinations(numbers, 2)
    results = set(map(lambda x: x[0] + x[1], combis))
    return sorted(results)