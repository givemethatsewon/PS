n = int(input())

cnt, number = 1, 666

while cnt < n:
    number += 1
    if '666' in str(number):
        cnt += 1
    
print(number)