from typing import *

def solution(sizes: List[List[int]]) -> int:
    # w, h 추출
    w = h = 0
    for size in sizes:
        w1, h1 = h2, w2 = size
        # 현재 w, h에 fit되는지 확인
        if (w >= w1 and h >= h1) or (w >= w2 and h >= h2):
            continue
    
        # w, h중 더 적게 늘려도 되는 경우 파악
        else:
            w1gap = w1 - w if w1 - w > 0 else 0
            h1gap = h1 - h if h1 - h > 0 else 0
            w2gap = w2 - w if w2 - w > 0 else 0 
            h2gap = h2 - h if h2 - h > 0 else 0
            
            if w1gap + h1gap  < w2gap + h2gap:
                w, h = max(w, w1), max(h, h1)
            else:
                w, h = max(w, w2), max(h, h2)
            
    return w * h