import sys
from collections import deque

# 명령의 수 N을 입력받음
n = int(sys.stdin.readline())

# 정수를 저장할 deque 생성
dq = deque()

# N번 반복하면서 명령을 처리
for _ in range(n):
    # 명령 한 줄을 읽어와 공백을 기준으로 분리
    command = sys.stdin.readline().split()
    cmd = int(command[0])

    if cmd == 1:
        # 1 X: 정수 X를 덱의 앞에 넣는다.
        dq.appendleft(int(command[1]))
    elif cmd == 2:
        # 2 X: 정수 X를 덱의 뒤에 넣는다.
        dq.append(int(command[1]))
    elif cmd == 3:
        # 3: 맨 앞의 정수를 빼고 출력 (없으면 -1)
        print(dq.popleft() if dq else -1)
    elif cmd == 4:
        # 4: 맨 뒤의 정수를 빼고 출력 (없으면 -1)
        print(dq.pop() if dq else -1)
    elif cmd == 5:
        # 5: 덱에 들어있는 정수의 개수 출력
        print(len(dq))
    elif cmd == 6:
        # 6: 덱이 비어있으면 1, 아니면 0 출력
        print(0 if dq else 1)
    elif cmd == 7:
        # 7: 맨 앞의 정수 출력 (없으면 -1)
        print(dq[0] if dq else -1)
    elif cmd == 8:
        # 8: 맨 뒤의 정수 출력 (없으면 -1)
        print(dq[-1] if dq else -1)