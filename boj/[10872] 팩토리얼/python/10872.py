# n 입력받기
n = int(input())

# n! 계산
result = 1
while n > 1:
    result = result * n
    n = n - 1

print(result)