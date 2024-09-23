from typing import *

def solution(array: List[int], commands: List[List[int]]) -> List[int]:
    ans: List[int] = []
    
    for command in commands:
        i, j, k = command
        ans.append(sorted(array[i-1:j])[k-1])
        
    return ans