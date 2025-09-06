import sys
input = sys.stdin.readline

n = int(input())

def prime_factors(x):
    factors = []
    
    divisor = 2
    while divisor * divisor <= x: # 제곱근까지 확인
        if x % divisor == 0:
            factors.append(divisor)
            x //= divisor
        else:
            divisor += 1

    # x는 이제 1과 자기 자신만 약수인 상태
    if x > 1:
        factors.append(x)
    
    factor_cnt = dict()
    for factor in factors:
        if factor not in factor_cnt:
            factor_cnt[factor] = 1
        else:
            factor_cnt[factor] += 1
        
    return factor_cnt # factor : cnt


for _ in range(n):
    a, b = map(int, input().rstrip().split())
    # 최소공배수 구하기
    # a, b를 소인수분해
    a_factor_cnt = prime_factors(a)
    b_factor_cnt = prime_factors(b)
    
    keys = set(a_factor_cnt.keys())
    keys.update(set(b_factor_cnt.keys()))
    keys = list(keys)
    # 겹치는 수 -> 더 큰 지수 채택, 안겹치는 수 -> 그냥 곱하기
    result = 1
    for key in keys:
        # a에만 있는 인수의 경우
        if key in a_factor_cnt and key not in b_factor_cnt:
            result *= key ** a_factor_cnt[key]
        # b에만 있는 인수의 경우
        elif key not in a_factor_cnt and key in b_factor_cnt:
            result *= key ** b_factor_cnt[key]
        # 둘 다 있는 경우
        else:
            result *= key ** max(a_factor_cnt[key], b_factor_cnt[key])
        
    print(result)