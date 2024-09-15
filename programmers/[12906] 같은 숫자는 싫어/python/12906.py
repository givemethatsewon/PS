def solution(arr):
    # 투 포인터
    answer = []
    left, right = 0, 1
    # arr의 길이가 1 이하면 그대로 return
    if len(arr) <= 1: 
        return arr
    
    # 일단 첫번째 숫자 집어넣기
    answer.append(arr[left])
    while right <= len(arr) - 1:
        # 왼쪽 숫자와 오른쪽 숫자가 다르면 오른쪽 숫자 집어넣기
        if arr[left] != arr[right]:
            answer.append(arr[right])
        left += 1
        right += 1
    
    # 끝에 다다르면 return
    return answer 
    
    