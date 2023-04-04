# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, prev):
            
            if not root:
                return
            
            cur = prev + root.val
            if cur == targetSum:
                count[0] += 1
                
            # includ
            dfs(root.left, cur)
            dfs(root.right, cur)
            
            # exclude
            if root not in visited:
                if root.val == targetSum:
                    count[0] += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
                
                visited.add(root)

        count = [0]
        if not root:
            return 0
        
        visited = {root}
        dfs(root, 0)
        
        return count[0]
            
            