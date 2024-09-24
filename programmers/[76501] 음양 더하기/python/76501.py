from typing import *

def solution(absolutes: List[int], signs: List[bool]) -> int:
    ans = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            ans += num
        else:
            ans -= num
    
    return ans