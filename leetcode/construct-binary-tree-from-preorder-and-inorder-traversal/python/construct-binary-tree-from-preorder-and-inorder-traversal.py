# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index_inorder = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:(root_index_inorder+1)], inorder[:root_index_inorder])
        root.right = self.buildTree(preorder[(root_index_inorder+1):], inorder[(root_index_inorder+1):])

        return root
        