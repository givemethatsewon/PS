import sys
input = sys.stdin.readline
# 테스트 케이스 입력
test_cases = int(input())

# 정수 입력받기
for _ in range(test_cases):
    n = int(input())
    # 엣지케이스 처리
    if n <= 2:
        print(2)
        continue
    
    elif n % 2 == 0:
        n += 1
    
    # 3 <= n <= 4 * 10^9
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            # 다음 n 초기화
            n += 2
            divisor = 3
        else:
            # 다음 divisor 테스트
            divisor += 2
    
    # 모든 divisor 통과한 n
    print(n)