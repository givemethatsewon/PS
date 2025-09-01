from collections import deque

# n 입력 받기
n = int(input())
# 종이(숫자) 배열 입력받기
nums = list(map(int, input().split()))
deq = deque((idx, num) for idx, num in enumerate(nums, start=1))

result = []
while deq:
    # 보고 터트리기
    popped = deq.popleft()
    result.append(popped[0])
    # 적혀있는 숫자만큼 회전(양수면 오른쪽으로 이동, 음수면 왼쪽으로 이동)
    deq.rotate(-popped[1]+1 if popped[1] > 0 else -popped[1])
    
print(*result)


