# 숫자 카드의 개수 입력으로
n = int(input())
# 숫자 카드에 적혀있는 정수들 
card_nums = set(map(int, input().split()))
# 숫자 카드인지 아닌지 구해야할 숫자들의 개수 입력으로
m = int(input())
# 숫자 카드인지 아닌지 구해야할 숫자 
target_nums = list(map(int, input().split()))
# M개의 0을 가진 리스트 초기화(정답 출력용)
ans = [0] * m


# 각 숫자(M개)에 대하여 순회
for i in range(m):
    # 해시로 카드에 있는지 없는지 확인
    if target_nums[i] in card_nums:
        ans[i] = 1
    
print(*ans)

