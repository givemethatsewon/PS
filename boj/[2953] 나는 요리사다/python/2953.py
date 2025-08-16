# 다섯 참가자의 입력 받기(5번 순회)
# 1등 누군지, 점수 정보 필요
winner, max_score = 1, 0
# 순회 중에 현재 max보다 크면 해당 선수로 1등과 점수 정보 업데이트
for i in range(5):
    line = input()
    current_score = sum(list(map(int, line.split())))
    if current_score > max_score:
        winner = i + 1
        max_score = current_score
    
print(winner, max_score)