# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        queue = deque()
        ans = []
        
        if root:
            queue.append(root)

        while queue:
            # 처리해야 할 노드만큼 반복
            nodes = []
            for i in range(len(queue)):
                # 큐에서 노드 꺼내기
                curr = queue.popleft()
                nodes.append(curr.val) # process
                
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
            # 반복문 종료 후 nodes의 스냅샷 ans에 넣기
            ans.append(nodes)
        
        return ans
