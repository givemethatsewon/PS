def solution(numbers):
    results = []
    for number in numbers:
        bin_str = bin(number)[2:]
        length = len(bin_str)
        
        # 최소한의 이진트리 높이 계산
        h = 0
        while (1 << h) - 1 < length:
            h += 1
        total_length = (1 << h) - 1
    
        padded_bin = bin_str.zfill(total_length)
        
        result = 1 if is_valid(padded_bin) else 0
        results.append(result)
        
    return results

def is_valid(binary: str) -> bool:
    # base case
    if len(binary) == 1:
        return True
    
    # 탐색
    mid = len(binary) // 2
    root = binary[mid]
    left = binary[:mid]
    right = binary[mid+1:]
    
    if root == '0':
        if '1' in binary:
            return False
        else: 
            return True
    else:
        return is_valid(left) and is_valid(right)
        