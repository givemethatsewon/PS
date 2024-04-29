import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
dic = {}

for i in range(1,n+1):
    name = input().rstrip()
    arr.append(name)
    dic[name] = i

for _ in range(m):
    q = input().rstrip()
    if q[0].isdigit():   #숫자
        print(arr[int(q)-1])
    else:
        print(dic[q])