# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        targetSum -= root.val
        
        if not root.left and not root.right:
            if targetSum == 0:
                return True
            else:
                return False

        if self.hasPathSum(root.left, targetSum):
            return True
        
        if self.hasPathSum(root.right, targetSum):
            return True
        
        