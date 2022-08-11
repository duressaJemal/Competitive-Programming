# Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        min_1 = root.val
        min_2 = float("inf")
        
        def dfs(node):
            
            nonlocal min_1, min_2
            
            if not node: return
            if min_1 < node.val < min_2:
                min_2 = node.val
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return -1 if min_2 == float("inf") else min_2
        
