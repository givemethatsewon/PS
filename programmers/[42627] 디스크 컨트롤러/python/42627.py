import heapq
from typing import *

def solution(jobs: List[List[int]]) -> int:
    # 각 작업에 대해 (요청시각, 소요시간, 작업번호)를 포함하도록 변환
    jobs = [(s, l, i) for i, (s, l) in enumerate(jobs)]
    # 요청시각 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    heap = []        # 처리 가능한 작업들을 저장하는 최소 힙 (우선순위: 소요시간, 요청시각, 작업번호)
    time = 0         # 현재 시각
    total_wait = 0   # 전체 반환 시간의 합
    idx = 0          # jobs 배열에서 아직 힙에 넣지 않은 작업의 인덱스
    count = 0        # 처리 완료된 작업 수
    n = len(jobs)

    while count < n:
        # 현재 시각 이전에 요청된 모든 작업을 힙에 추가
        while idx < n and jobs[idx][0] <= time:
            s, l, i = jobs[idx]
            heapq.heappush(heap, (l, s, i))
            idx += 1
        
        # 힙에 작업이 있다면 우선순위에 따라 꺼내서 처리
        if heap:
            l, s, i = heapq.heappop(heap)
            time += l                 # 작업 수행 후 시각 업데이트
            total_wait += time - s    # (완료시각 - 요청시각) 만큼 반환 시간에 누적
            count += 1
        else:
            # 대기 큐에 작업이 없으면 다음 작업이 도착할 때까지 시간을 이동
            time = jobs[idx][0]
    
    # 모든 작업의 평균 반환 시간의 정수 부분 반환
    return total_wait // n

    
