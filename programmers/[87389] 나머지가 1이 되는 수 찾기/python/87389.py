from typing import *

def solution(n: int) -> int:
    for x in range(2, n):
        if n % x == 1:
            return x