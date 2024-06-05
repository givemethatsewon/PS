# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        visited = []
        inorder(root, visited)
        return visited
