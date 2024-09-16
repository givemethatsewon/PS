from typing import *

def solution(participant: List[str], completion: List[str]) -> str:
    # 완주 여부 매핑 테이블
    results: dict = {}
    
    # 참가자들 삽입
    for p in participant:
        if p in results:
            results[p] += 1
        else:
            results[p] = 1
        
        
    # 완주결과 삽입
    for c in completion:
        results[c] -= 1
    
    # 완주 못한 참가자 확인
    for person, remain in results.items():
        if remain:
            return person
        
    