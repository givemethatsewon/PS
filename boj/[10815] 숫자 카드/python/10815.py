# 숫자 카드의 개수 입력으로
n = int(input())
# 숫자 카드에 적혀있는 정수들 
card_nums = list(map(int, input().split()))
# 이분탐색 예정이므로 정렬
card_nums.sort()
# 숫자 카드인지 아닌지 구해야할 숫자들의 개수 입력으로
m = int(input())
# 숫자 카드인지 아닌지 구해야할 숫자 
target_nums = list(map(int, input().split()))
# M개의 0을 가진 리스트 초기화(정답 출력용)
ans = [0] * m

# binary search 구현
def bin_search(target) -> bool:
    start, end = 0, n - 1    
    while start <= end:
        mid = (start + end) // 2
        if card_nums[mid] < target:
            start = mid + 1
        elif target < card_nums[mid]:
            end = mid - 1
        else:
            return True
    
    return False
    

# 각 숫자(M개)에 대하여 순회
idx = 0
for num in target_nums:
    # 이분 탐색으로 있는지 없는지 확인
    if(bin_search(num)):
        # 있으면 해당 인덱스 1로 수정
        ans[idx] = 1
    idx += 1
    
print(*ans)

