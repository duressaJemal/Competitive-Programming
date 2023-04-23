# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        
        def dfs(node):
            if not node:
                return "c"
            
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == "nc" or right == "nc":
                self.answer  += 1
                return "p"
            
            if left == "p" or right == "p":
                return "c"
            
            if node != root:
                return "nc"
            self.answer += 1
            return "p"
    
        
        dfs(root)
        return self.answer
            
                
            
            
                
        
        