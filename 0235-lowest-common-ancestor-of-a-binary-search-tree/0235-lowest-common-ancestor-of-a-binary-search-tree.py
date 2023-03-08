# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N)
# Space: O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            
            # current node is ancestor
            if root.val == p.val or root.val == q.val:
                return root
            if (p.val > root.val or q.val > root.val) and (p.val < root.val or q.val < root.val):
                return root
            
            # ancestor in the right node
            if p.val > root.val: 
                return dfs(root.right, p, q)
            # ancestor in the left node
            else:                
                return dfs(root.left, p, q)
        
        return dfs(root, p, q)
            
            