x = int(input())

def accum_sum(n):
    return int(n*(n + 1) / 2)

# 누적 합 기준으로 속하는 구간 판단
i = 1
while x > accum_sum(i):
    i += 1

gap = x - accum_sum(i-1)

if i % 2 == 0:
    a = gap
    b = i + 1 - gap
else:
    a = i + 1 - gap
    b = gap

print(f"{a}/{b}")



