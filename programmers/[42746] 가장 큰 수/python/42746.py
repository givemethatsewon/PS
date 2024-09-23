from typing import *

def solution(numbers: List[int]) -> str:
    numbers_str: List[str] = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    result: str = ''.join(numbers_str)
    
    # 모든 숫자가 0인 경우 '0'을 반환
    return '0' if result[0] == '0' else result
    
    