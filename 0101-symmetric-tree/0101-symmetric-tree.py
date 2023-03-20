# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N)
# Space: O(N)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            
            if not root1: return root2 == None
            if not root2: return root1 == None
            
            if root1.val != root2.val: return False
            
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        
        if root.left or root.right:
            return dfs(root.left, root.right)
        return True
        
        