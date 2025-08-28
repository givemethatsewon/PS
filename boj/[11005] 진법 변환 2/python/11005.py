n, b = map(int, input().split())

# 10진법 수 n, b진법으로
# 0:0, 10:A, 35:Z인 dict 생성
n_to_b_map = dict()
for i in range(b):
    if i < 10:
        n_to_b_map[i] = str(i)
    else:
        n_to_b_map[i] = chr(ord('A') + i - 10)

# b로 n나누면서 나머지를 key로 해서 append
converted = []
while n > 0:
    converted.append(n_to_b_map[n % b])
    n = n // b

# 역순으로 순회하면서 str 만들기
converted = converted[::-1]
result = ''.join(converted)

print(result)


