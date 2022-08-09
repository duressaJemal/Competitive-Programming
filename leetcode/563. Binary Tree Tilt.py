# link: https://leetcode.com/problems/binary-tree-tilt/submissions/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        SUM = 0
    
        def dfs(node):
            
            nonlocal SUM
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            SUM += abs(left - right)
            return  node.val + left + right
        
        dfs(root)
        
        return SUM


# BFS

# time:
# space:

# class Solution:
#     def findTilt(self, root: Optional[TreeNode]) -> int:
     

