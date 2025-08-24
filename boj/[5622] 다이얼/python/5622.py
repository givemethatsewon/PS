# 알파벳 그룹을 리스트로 정의
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# 단어 입력받기
word = input()

# 총 시간을 저장할 변수 초기화
total_time = 0

# 입력받은 단어의 각 문자를 하나씩 확인
for char in word:
    # dial 리스트의 각 그룹을 확인
    for i in range(len(dial)):
        # 현재 문자가 그룹에 포함되어 있다면
        if char in dial[i]:
            # 시간을 계산하여 더함
            # 인덱스(i)는 0부터 시작하고, 숫자 2는 인덱스 0에 해당
            # 걸리는 시간은 (숫자 + 1)초 이므로, (i + 2) + 1 = i + 3초
            total_time += i + 3
            break # 해당 문자의 그룹을 찾았으면 다음 문자로 넘어감

# 최종 결과 출력
print(total_time)