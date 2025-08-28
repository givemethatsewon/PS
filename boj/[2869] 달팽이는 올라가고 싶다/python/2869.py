a, b, v = map(int, input().split())

# v-a까지 (a-b)로 얼마나 걸릴까?
day, remainder = (v - a) // (a - b), (v - a) % (a - b)

if remainder != 0:
    day += 1
day += 1

print(day)


