from typing import *

class TrieNode:
    def __init__(self):
        self.children: dict = {}
        self.end: bool = False
    
class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()
    
    # 삽입 과정에서 접두어가 있으면 False 반환
    def insert(self, numbers) -> bool:
        curr: TrieNode = self.root
        for number in numbers:
            if number not in curr.children:
                curr.children[number] = TrieNode()
            curr = curr.children[number]
            
            # 이미 다른 번호가 접두어로 존재하는 경우
            if curr.end:
                return False
        
        # 해당 번호가 다른 번호의 접두어인 경우
        if curr.children:
            return False
        
        # 번호 삽입 완료
        curr.end = True
        return True


def solution(phone_book: List[str]) -> bool: 
    phone_trie: Trie = Trie()     # 전화번호 Trie
    # 전화번호를 Trie에 집어넣기
    for phone_number in phone_book:
        if not phone_trie.insert(phone_number):
            return False
    
    return True
        
    
        
        
        