from collections import deque
import heapq
from typing import *

def solution(priorities: List[int], location: int) -> int:
    nth: int = 0    # 처리 순서
    pointer = 0     # 처리 포인터
    max_heap = [-1 * priority for priority in priorities]
    heapq.heapify(max_heap)
    # priority 힙
    
    # 운영체제의 처리
    for _ in range(len(priorities)):
        nth += 1
        # 우선순위 최대값
        max = -1 * heapq.heappop(max_heap)
        
        # 처음으로 같은 것 0으로 마킹(처리)
        while True:
            if max == priorities[pointer]:
                priorities[pointer] = 0
                break
            pointer += 1
            pointer = pointer % len(priorities)

            
        if pointer == location: 
            return nth
    
    