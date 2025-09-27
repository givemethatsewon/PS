import sys
from math import factorial

input = sys.stdin.readline

def comb_cnt(a, b):
    return factorial(a) // (factorial(b) * factorial(a - b))


# 테스트 케이스 개수 입력
t_cnt = int(input())
# 테스트 케이스만큼 반복
for _ in range(t_cnt):
    # 왼쪽, 오른쪽 입력
    n, m = map(int, input().strip().split())
    # 가능한 경우의 수 mCn
    print(comb_cnt(m, n))
    