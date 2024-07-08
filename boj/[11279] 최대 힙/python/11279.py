import heapq
from sys import stdin

input = stdin.readline
N = int(input())    # 연산의 개수
arr = list()


for _ in range(N):
    x = int(input())
    if x == 0:
        # 배열에서 가장 큰 값을 출력. 비어있다면 0을 출력
        if len(arr) == 0: 
            print(0)
            continue
        print(-1 * heapq.heappop(arr)) 
        
    else:
        # x를 배열에 넣기
        heapq.heappush(arr, -1 * x)