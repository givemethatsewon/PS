from typing import *

def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    answer: List[int] = []
    progresses = progresses[::-1]
    speeds = speeds[::-1]
    
    while len(speeds) > 0:
        # 하루 기준
        cnt = 0
        
        for i in range(len(progresses)):
            # 각 speed를 progress에 더해주기
            progresses[i] += speeds[i]

        # 진행률 100 넘은 일 있는지 뒤에서부터 확인
        for progress in reversed(progresses):
            if progress >= 100:
                progresses.pop()
                speeds.pop()
                cnt += 1
            else:
                break
        
        if cnt != 0:
            answer.append(cnt)
            
    return answer