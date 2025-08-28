#n, m 입력 받기
n, m = map(int, input().split())

word_set = set()
word_list = list()
# n번 순회하면서 set에 문자열 저장
for _ in range(n):
   word_set.add(input())
# m번 순회하면서 list에 문자열 저장
for _ in range(m):
    word_list.append(input())
# list 순회하며서 set에 있는지 체크

cnt = 0
for word in word_list:
    if word in word_set: cnt += 1

print(cnt)