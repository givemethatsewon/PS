def solution(s: str) -> bool:
    
    remain = [letter for letter in s] # 남아있는 괄호
    closing = [] # 꺼낸 괄호
    
    # remain이 끝날때까지 체크
    while len(remain) > 0:
        # remain 체크
        bracket = remain.pop()
        # ) 의 경우 remain에서 closing로 옮기기
        if bracket == ')':
            closing.append(bracket)
        # ( 의 경우
        elif bracket == '(':
            # closing이 비어 있으면 false 리턴
            if not closing:
                return False
            # ) 의 경우 match
            else:
                closing.pop()
                
    # remain, closing모두 비어있으면 true 리턴
    if len(closing) == 0:
        return True
    # 아니면 false 리턴
    else:   
        return False
        