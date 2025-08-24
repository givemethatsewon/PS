import sys

# 표준 입력(stdin)의 모든 줄을 읽어서 line 변수에 하나씩 넣으며 반복
for line in sys.stdin:
    # 입력받은 line에 이미 포함된 줄바꿈 문자가 중복되지 않도록 end=''를 사용
    print(line, end='')
