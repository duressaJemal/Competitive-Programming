# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root):
            
            if not root: return []
            left = dfs(root.left)
            right = dfs(root.right)
            
            return left + [root.val] + right
        
        return dfs(root)[k - 1]
            
            