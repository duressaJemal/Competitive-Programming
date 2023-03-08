# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N)
# Space: O(N)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            
            if not q: return p == None
            if not p: return q == None
            
            if p.val != q.val: return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
    
        return dfs(p, q)
            
            