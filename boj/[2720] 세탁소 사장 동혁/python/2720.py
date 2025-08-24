# 테스트 케이스 개수 입력
T = int(input())

cnt = 0
coins = [25, 10, 5, 1]

# 테스트 케이스 입력만큼 순회
for _ in range(T):
    ans = [0, 0, 0, 0]
    money = int(input())
    # 쿼터, 다임, 니켈, 페니 순서대로 필요한 잔돈 계산
    for i in range(4):
        # 몫 -> 동전 개수 count
        cnt = money // coins[i]
        ans[i] = cnt
        # 나머지 -> 다음 동전 종류에 토스
        money = money - cnt *  coins[i]
        cnt =0
    print(*ans)
        
# 동전 개수 출력
