from typing import * 

def solution(answers: List[int]) -> List[int]:
    one_ans = [1, 2, 3, 4, 5] 
    two_ans = [2, 1, 2, 3, 2, 4, 2, 5]    
    three_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
    ans_cnt = [0, 0, 0]
    # 맞았으면 정답 + 1
    # answers의 개수가 반복 패턴보다 훨씬 많을 수 있다
    
    for i in range(len(answers)):
        ans = answers[i]
        
        if ans == one_ans[i % len(one_ans)]: ans_cnt[0] += 1
        if ans == two_ans[i % len(two_ans)]: ans_cnt[1] += 1
        if ans == three_ans[i % len(three_ans)]: ans_cnt[2] += 1
        
    max_ans_cnt = max(ans_cnt)
    result = []
    for i in range(len(ans_cnt)):
        if ans_cnt[i] == max_ans_cnt: 
            result.append(i + 1)
    
    return sorted(result)
    
        
        
        