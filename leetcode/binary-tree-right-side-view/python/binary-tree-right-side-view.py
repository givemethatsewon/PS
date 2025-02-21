# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def rightSideView(self, root):
        queue = deque()
        ans = []

        if root:
            queue.append(root)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft() # 현재 node
                if i == 0:
                    ans.append(curr.val) # process
                
                if curr.right:
                    queue.append(curr.right) # 오른쪽부터 담기
                if curr.left:
                    queue.append(curr.left)
        
        return ans
            
        