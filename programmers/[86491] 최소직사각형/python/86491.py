from typing import *

def solution(sizes: List[List[int]]) -> int:
    w_ans, h_ans = 0, 0
    for w, h in sizes:
        w, h = max(w, h), min(w, h)
        
        w_ans = max(w, w_ans)
        h_ans = max(h, h_ans)
    
    return w_ans * h_ans
            
        
    