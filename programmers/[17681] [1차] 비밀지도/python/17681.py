from typing import *


def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    # 비밀지도1 해석
    ans: List[str] = []
    for num1, num2 in zip(arr1, arr2):
        step = []
        for i in range(n):
            curr1 = num1 % 2
            num1 = num1 // 2
            curr2 = num2 % 2
            num2 = num2 // 2
            
            if curr1 or curr2:
                step.append("#")
            else:
                step.append(" ")
        ans.append("".join(reversed(step)))
    return ans
            
        
        