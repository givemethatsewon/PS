from collections import deque


class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        oldToNew = {}   # 기존 노드와 복사한 노드를 매핑
        queue = deque()    # 방문 순서를 저장
        
        #edge case
        if not node:
            return None
        
        queue.append(node)
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                
                copy = None
                if current in oldToNew:
                    copy = oldToNew[current]
                else:
                    copy = Node(current.val) # 값 복사
                    oldToNew[current] = copy
                    
                    
                for nei in current.neighbors:
                    if nei not in oldToNew:
                        queue.append(nei) # 인접 리스트에 있는 애들 큐에 집어넣어서 다음 순서에 탐색
                        oldToNew[nei] = Node(nei.val)
                        
                    copy.neighbors.append(oldToNew[nei])
                
        return oldToNew[node]