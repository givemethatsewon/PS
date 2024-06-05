# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def inOrder(node, arr):
            if not node:
                return
            inOrder(node.left, arr)
            arr.append(node.val)
            inOrder(node.right, arr)

        visited = []
        inOrder(root, visited)
        return visited[k-1]

            
        