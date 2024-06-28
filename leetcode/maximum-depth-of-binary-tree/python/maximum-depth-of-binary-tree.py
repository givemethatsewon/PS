class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        m = d = 1
        def dfs(node, max_depth, depth):
            if not node:
                return max_depth
            
            if depth > max_depth:
                max_depth += 1
                
            
            l = dfs(node.left, max_depth, depth + 1)
            r = dfs(node.right, max_depth, depth + 1)
            max_depth = max(l, r)
            
            return max_depth
        
        return dfs(root, m, d)