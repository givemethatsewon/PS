from typing import *

def solution(clothes: List[List[str]]) -> int:
    category_cnt: Dict[str, int] = dict()
    
    # 옷 카테고리별로 개수 저장
    for cloth, category in clothes:
        if category not in category_cnt:
            category_cnt[category] = 0
        category_cnt[category] += 1
        
    # 경우의 수 계산
    total: int = 1
    for count in category_cnt.values():
        total *= (count + 1) # +1 해서 각 카테고리에서 입지 않는 경우도 고려
    
    # 아무것도 입지 않는 경우 제외
    return total - 1
            
    
        
    