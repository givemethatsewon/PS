# 1. 두 수 a, b가 있다
# 2. a를 b로 나눈 나머지를 구한다
# 3. 만약 r이 0이라면, b가 최대공약수이다
# 4. 만약 r이 0이 아니라면, a자리에 b를, b자리에 r을 놓고 2번을 반복한다.

n1, n2 = map(int, input().split())
a, b = max(n1, n2), min(n1, n2)

while a % b != 0:
    a, b = b, a % b

# 두 수의 곱 = 최대공약수 X 최소공배수
print(int(n1 * n2 / b))