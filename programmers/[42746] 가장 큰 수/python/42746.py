from typing import *

def solution(numbers: List[int]) -> str:
    # 문자열로 리스트로 변환
    numbers_str: List[str] = list(map(str, numbers))
    
    max_len = len(str(max(numbers))) # 가장 큰 숫자의 자리수
    numbers_str.sort(key=lambda x: x*max_len, reverse=True) # 자리수를 맞춰서 문자열 아스키 코드 비교
    result: str = ''.join(numbers_str)
    
    # 모든 숫자가 0인 경우 '0'을 반환
    return '0' if result[0] == '0' else result
    
    