import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    spicy = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        small1 = heapq.heappop(scoville)
        small2 = heapq.heappop(scoville)
        
        mixed = small1 + small2 * 2
        
        heapq.heappush(scoville, mixed)
        answer += 1
    
    return answer