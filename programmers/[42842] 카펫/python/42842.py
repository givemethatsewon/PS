from typing import *
from math import sqrt

def solution(brown: int, yellow: int) -> List[int]:
    # yellow = w * h 파악
    # w >= h인 경우만 거르기
    candidates = []
    for h in range(1, int(sqrt(yellow) + 1)):
        if yellow % h == 0:
            candidates.append((yellow // h, h)) # (w, h) 튜플로 삽입
    print(candidates)
    # brown = w*2 + 2*h + 4 만족하는 케이스 찾기
    for w, h in candidates:
         if brown == w*2 + 2*h + 4:
                return [w+2, h+2]
        