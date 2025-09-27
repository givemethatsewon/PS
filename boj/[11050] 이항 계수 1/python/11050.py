# n, k 입력 받기
n, k = map(int, input().split())

# 이항계수 구하기 n! / k! * (n-k)! 
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

print(int(factorial(n) / (factorial(k) * factorial(n-k))))