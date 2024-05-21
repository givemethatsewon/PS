# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def findMaxValue(root):
    current = root
    while current and current.right: # current는 current.right이 유효하기 위한 조건
        current = current.right
    return current


class Solution:
    def deleteNode(self, root, key):
        # base condition
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:  # key == root.val
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # find the max value int left hand side
                max_node = findMaxValue(root.left)
                root.val = max_node.val  # 나보다 작지만 그 중에선 제일 큰 걸로 변경 -> BST 규칙 유지됨
                root.left = self.deleteNode(root.left, max_node.val)  # 중복 없애야 하므로 삭제

        return root

        