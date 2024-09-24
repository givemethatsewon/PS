from typing import *

def solution(N: int, stages: List[int]) -> List[int]:
    # N: 전체 스테이지 수 (1~N)
    # stages: 사용자가 현재 멈춰있는 스테이지
    # 실패율 = 스테이지 도달 and 아직 클리어 X 플레이어 수 / 스테이지에 도달
    stay_cnt = {}
    for k in range(1, N+2):
        stay_cnt[k] = 0
        
    for stage in stages:
        stay_cnt[stage] += 1
    
    failure_rates = {}
    for i in range(1, N + 1):      
        div = sum([stay_cnt[j] for j in range(i, N + 2)])
        if div != 0:
            failure_rates[i] = stay_cnt[i] / div 
        else:
            failure_rates[i] = 0
        
        
    sorted_rates = sorted(failure_rates.items(), key=lambda x : (-x[1], x[0]))
    return list(map(lambda x:x[0], sorted_rates))
    
        
    
    