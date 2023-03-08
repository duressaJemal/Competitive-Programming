# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = [None]
        
        def dfs(root, p, q):
            if not root: return 0
            
            curr = 0
            if root.val == p.val or root.val == q.val:
                curr = 1
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if (curr + left + right) > 1:
                ans[0] = root
            
            return curr or left or right
        
        dfs(root, p, q)
        return ans[0]
        
        