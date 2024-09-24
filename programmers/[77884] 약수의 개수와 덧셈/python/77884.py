def solution(left: int, right: int) -> int:
    ans = 0
    
    for num in range(left, right + 1): 
        cnt = 0
        for k in range(1, int(num**(0.5)) + 1):
            if num % k == 0:
                if k ** 2 == num:
                    cnt += 1 
                else:
                    cnt += 2
        if cnt % 2 == 0:
            ans += num
        else:
            ans -= num
    
    return ans
        
    

    