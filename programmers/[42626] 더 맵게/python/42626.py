from typing import *
import heapq

def solution(scovile: List[int] , K: int) -> int:
    heapq.heapify(scovile)
    
    cnt = 0 # 섞은 횟수
    # 모든 음식의 스코빌 지수가 K 이상이 될 때까지
    n = heapq.heappop(scovile)
    while n < K:
        # 모든 음식의 스코빌 지수를 k 이상으로 만들 수 없는 경우
        if len(scovile) == 0:
            return -1
        
        cnt += 1    # 횟수 증가
        # scovile 교체
        new_scovile = n + heapq.heappop(scovile) * 2
        heapq.heappush(scovile, new_scovile)
        n = heapq.heappop(scovile)
    
    
    return cnt