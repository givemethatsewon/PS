def solution(n, times):
    # n: 입국 심사를 기다리는 사람 수
    # times: 각 심사관이 한명을 심사하는 데 걸리는 시간들
    # return: 모든 사람이 심사를 받는데 걸리는 시간의 최솟값
    left = 1    # 최소 시간
    right = max(times) * n  # 최대 시간
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // time for time in times)  # mid 시간 내 처리할 수 있는 사람의수 합
        
        if total >= n:  # 아직 여유 O, 시간 더 줄여도 됨
            answer = mid    # 가능한 최소 시간 update
            right = mid - 1
        else:
            left = mid + 1
    return answer