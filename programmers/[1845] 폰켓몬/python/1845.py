from typing import *

def solution(nums: List[int]) -> int:
    # 뽑을 포켓몬 마리수
    total: int = int(len(nums) / 2)
    
    # 중복 삭제해서 count
    num_set = len(set(nums))
    
    # total과 비교 후 return
    return num_set if num_set <= total else total
    