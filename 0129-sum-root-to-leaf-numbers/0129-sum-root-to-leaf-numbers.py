# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, total):
            
            if not root:
                return
            
            if not root.left and not root.right:
                total += str(root.val)
                result[0] += int(total)
                return
            
            dfs(root.left, total + str(root.val))
            dfs(root.right, total + str(root.val))
            
            return
        
        result = [0]
        dfs(root, "")
        return result[0]
        
        