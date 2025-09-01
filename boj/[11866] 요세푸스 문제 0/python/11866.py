from collections import deque

# n과 k 입력 받기
n, k = map(int, input().split())
# 덱 사용 
queue = deque(i for i in range(1, n+1))

# -> cnt 1++하고 popleft, cnt가 k면 그대로 제거하고 cnt 0으로 초기화
# -> cnt가 k가 아니면 다시 append
# 큐가 비면 종료
result = []
cnt = 0
while queue:
    person = queue.popleft()
    cnt += 1
    if cnt == k:
        result.append(str(person))
        cnt = 0
        continue
    queue.append(person)

result_str = ', '.join(result)
print(f"<{result_str}>")